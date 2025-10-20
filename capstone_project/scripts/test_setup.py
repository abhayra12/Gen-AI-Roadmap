"""
Quick Test Script for Manufacturing Copilot
Tests HuggingFace endpoints and basic functionality
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_env_variables():
    """Test that required environment variables are set."""
    print("=" * 60)
    print("TESTING ENVIRONMENT VARIABLES")
    print("=" * 60)
    
    required_vars = [
        "HUGGINGFACE_TOKEN",
        "VLM_MODEL_ID",
        "LLM_MODEL_ID",
        "EMBEDDING_MODEL_ID"
    ]
    
    all_good = True
    for var in required_vars:
        value = os.getenv(var)
        if value:
            # Mask the token for security
            display_value = value if var != "HUGGINGFACE_TOKEN" else f"{value[:10]}...{value[-4:]}"
            print(f"✅ {var}: {display_value}")
        else:
            print(f"❌ {var}: NOT SET")
            all_good = False
    
    print()
    return all_good


def test_huggingface_connection():
    """Test connection to HuggingFace."""
    print("=" * 60)
    print("TESTING HUGGINGFACE CONNECTION")
    print("=" * 60)
    
    try:
        from huggingface_hub import HfApi
        
        api = HfApi()
        token = os.getenv("HUGGINGFACE_TOKEN")
        
        # Test authentication
        user_info = api.whoami(token=token)
        print(f"✅ HuggingFace Authentication: SUCCESS")
        print(f"   Logged in as: {user_info.get('name', 'Unknown')}")
        print()
        return True
        
    except Exception as e:
        print(f"❌ HuggingFace Connection: FAILED")
        print(f"   Error: {str(e)}")
        print()
        return False


def test_embeddings():
    """Test HuggingFace embeddings."""
    print("=" * 60)
    print("TESTING EMBEDDINGS MODEL")
    print("=" * 60)
    
    try:
        from langchain_community.embeddings import HuggingFaceEmbeddings
        
        model_id = os.getenv("EMBEDDING_MODEL_ID", "sentence-transformers/all-MiniLM-L6-v2")
        print(f"📦 Loading model: {model_id}")
        
        embeddings = HuggingFaceEmbeddings(
            model_name=model_id,
            model_kwargs={'device': 'cpu'}
        )
        
        # Test embedding generation
        test_text = "This is a test of the embedding model"
        embedding = embeddings.embed_query(test_text)
        
        print(f"✅ Embeddings: SUCCESS")
        print(f"   Embedding dimension: {len(embedding)}")
        print()
        return True
        
    except Exception as e:
        print(f"❌ Embeddings: FAILED")
        print(f"   Error: {str(e)}")
        print()
        return False


def test_llm_endpoint():
    """Test HuggingFace LLM endpoint."""
    print("=" * 60)
    print("TESTING LLM ENDPOINT")
    print("=" * 60)
    
    try:
        from langchain_huggingface import HuggingFaceEndpoint
        
        model_id = os.getenv("LLM_MODEL_ID", "meta-llama/Llama-2-7b-chat-hf")
        token = os.getenv("HUGGINGFACE_TOKEN")
        
        print(f"📦 Connecting to model: {model_id}")
        print("⏳ This may take 30-60 seconds on first connection...")
        
        llm = HuggingFaceEndpoint(
            repo_id=model_id,
            huggingfacehub_api_token=token,
            temperature=0.7,
            max_new_tokens=100,
            timeout=60,
        )
        
        # Test inference
        test_prompt = "Write a one-sentence description of a CNC machine."
        response = llm.invoke(test_prompt)
        
        print(f"✅ LLM Endpoint: SUCCESS")
        print(f"   Test prompt: {test_prompt}")
        print(f"   Response: {response[:100]}...")
        print()
        return True
        
    except Exception as e:
        print(f"❌ LLM Endpoint: FAILED")
        print(f"   Error: {str(e)}")
        print()
        return False


def test_chromadb():
    """Test ChromaDB setup."""
    print("=" * 60)
    print("TESTING CHROMADB")
    print("=" * 60)
    
    try:
        from langchain_community.vectorstores import Chroma
        from langchain_community.embeddings import HuggingFaceEmbeddings
        
        embeddings = HuggingFaceEmbeddings(
            model_name=os.getenv("EMBEDDING_MODEL_ID", "sentence-transformers/all-MiniLM-L6-v2"),
            model_kwargs={'device': 'cpu'}
        )
        
        # Create a temporary collection
        vectorstore = Chroma(
            collection_name="test_collection",
            embedding_function=embeddings,
            persist_directory="./test_chroma_db"
        )
        
        print(f"✅ ChromaDB: SUCCESS")
        print(f"   Vector store initialized")
        print()
        
        # Cleanup
        import shutil
        shutil.rmtree("./test_chroma_db", ignore_errors=True)
        
        return True
        
    except Exception as e:
        print(f"❌ ChromaDB: FAILED")
        print(f"   Error: {str(e)}")
        print()
        return False


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("MANUFACTURING COPILOT - SYSTEM TEST")
    print("=" * 60 + "\n")
    
    results = []
    
    # Test 1: Environment Variables
    results.append(("Environment Variables", test_env_variables()))
    
    # Only proceed if env vars are set
    if not results[0][1]:
        print("\n❌ Cannot proceed without required environment variables.")
        print("   Please ensure .env file exists with HUGGINGFACE_TOKEN set.")
        return
    
    # Test 2: HuggingFace Connection
    results.append(("HuggingFace Connection", test_huggingface_connection()))
    
    # Test 3: Embeddings
    results.append(("Embeddings Model", test_embeddings()))
    
    # Test 4: LLM Endpoint (this takes longer)
    results.append(("LLM Endpoint", test_llm_endpoint()))
    
    # Test 5: ChromaDB
    results.append(("ChromaDB", test_chromadb()))
    
    # Summary
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    total = len(results)
    passed = sum(1 for _, p in results if p)
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All systems operational! Ready for production.")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please review errors above.")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
