"""
Analytics Agent - Data-Driven Insights from BigQuery
Provides historical trends, comparative analysis, and KPI calculations
"""

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
import pandas as pd

logger = logging.getLogger(__name__)


class AnalyticsAgent:
    """
    Analytics Agent for data-driven insights
    Queries BigQuery for historical trends and comparative analysis
    """
    
    def __init__(self, bigquery_client=None):
        """
        Initialize Analytics Agent
        
        Args:
            bigquery_client: Google BigQuery client (optional for development)
        """
        self.bq_client = bigquery_client
        self.mock_mode = bigquery_client is None
        
        if self.mock_mode:
            logger.warning("Running in MOCK mode (no BigQuery client)")
            logger.info("Install google-cloud-bigquery and provide credentials for production")
        else:
            logger.info("Analytics Agent initialized with BigQuery client")
    
    async def analyze_performance_trend(
        self,
        equipment_id: str,
        time_range: str = "last_30_days"
    ) -> Dict[str, Any]:
        """
        Analyze equipment performance trends over time
        
        Args:
            equipment_id: Equipment identifier
            time_range: Time range for analysis (last_7_days, last_30_days, last_90_days)
            
        Returns:
            Dictionary with performance metrics and trends
        """
        logger.info(f"Analyzing performance trend for {equipment_id} ({time_range})")
        
        if self.mock_mode:
            return self._mock_performance_trend(equipment_id, time_range)
        
        # TODO: Implement actual BigQuery query
        # query = f"""
        # SELECT
        #     DATE(timestamp) as date,
        #     AVG(temperature) as avg_temperature,
        #     AVG(vibration) as avg_vibration,
        #     AVG(pressure) as avg_pressure,
        #     COUNT(*) as reading_count
        # FROM `project.dataset.sensor_readings`
        # WHERE equipment_id = '{equipment_id}'
        #   AND timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL {days} DAY)
        # GROUP BY date
        # ORDER BY date
        # """
        
        return self._mock_performance_trend(equipment_id, time_range)
    
    def _mock_performance_trend(self, equipment_id: str, time_range: str) -> Dict[str, Any]:
        """Generate mock performance trend data"""
        
        # Parse time range
        if time_range == "last_7_days":
            days = 7
        elif time_range == "last_30_days":
            days = 30
        elif time_range == "last_90_days":
            days = 90
        else:
            days = 30
        
        # Generate mock historical data
        import numpy as np
        
        base_temp = 67.0
        base_vibration = 2.5
        base_pressure = 45.0
        
        # Simulate gradual degradation over time
        trend_factor = np.linspace(1.0, 1.15, days)  # 15% increase over period
        
        historical_data = {
            'avg_temperature': base_temp * trend_factor,
            'avg_vibration': base_vibration * trend_factor,
            'avg_pressure': base_pressure / trend_factor,  # Pressure decreases
        }
        
        # Calculate current vs previous period metrics
        current_period_temp = historical_data['avg_temperature'][-7:].mean()
        previous_period_temp = historical_data['avg_temperature'][-14:-7].mean()
        temp_change = ((current_period_temp - previous_period_temp) / previous_period_temp) * 100
        
        current_period_vib = historical_data['avg_vibration'][-7:].mean()
        previous_period_vib = historical_data['avg_vibration'][-14:-7].mean()
        vib_change = ((current_period_vib - previous_period_vib) / previous_period_vib) * 100
        
        current_period_pres = historical_data['avg_pressure'][-7:].mean()
        previous_period_pres = historical_data['avg_pressure'][-14:-7].mean()
        pres_change = ((current_period_pres - previous_period_pres) / previous_period_pres) * 100
        
        # Calculate uptime (mock)
        uptime = np.random.uniform(88, 95)
        prev_uptime = np.random.uniform(90, 96)
        uptime_change = uptime - prev_uptime
        
        # Calculate defect rate (mock)
        defect_rate = np.random.uniform(1.5, 3.5)
        prev_defect_rate = np.random.uniform(1.0, 2.5)
        defect_change = defect_rate - prev_defect_rate
        
        # Determine trend direction
        def trend_arrow(change):
            if change > 1:
                return "↑ Increasing"
            elif change < -1:
                return "↓ Decreasing"
            else:
                return "→ Stable"
        
        result = {
            "equipment_id": equipment_id,
            "analysis_type": "performance_trend",
            "time_range": time_range,
            "period_days": days,
            
            "current_metrics": {
                "avg_uptime": f"{uptime:.1f}%",
                "avg_temperature": f"{current_period_temp:.1f}°C",
                "avg_vibration": f"{current_period_vib:.2f} mm/s",
                "avg_pressure": f"{current_period_pres:.1f} PSI",
                "defect_rate": f"{defect_rate:.1f}%"
            },
            
            "trends": {
                "uptime": f"{trend_arrow(uptime_change)} ({uptime_change:+.1f}% vs previous period)",
                "temperature": f"{trend_arrow(temp_change)} ({temp_change:+.1f}% vs previous period)",
                "vibration": f"{trend_arrow(vib_change)} ({vib_change:+.1f}% vs previous period)",
                "pressure": f"{trend_arrow(pres_change)} ({pres_change:+.1f}% vs previous period)",
                "defect_rate": f"{trend_arrow(defect_change)} ({defect_change:+.1f}% vs previous period)"
            },
            
            "insights": self._generate_insights(
                temp_change, vib_change, pres_change, uptime_change, defect_change
            ),
            
            "confidence": 0.80,
            "data_source": "Mock Data (Development Mode)"
        }
        
        return result
    
    def _generate_insights(
        self,
        temp_change: float,
        vib_change: float,
        pres_change: float,
        uptime_change: float,
        defect_change: float
    ) -> List[str]:
        """Generate insights from trend data"""
        
        insights = []
        
        # Temperature insights
        if temp_change > 5:
            insights.append("🔥 Significant temperature increase detected - may indicate cooling system degradation")
        elif temp_change > 2:
            insights.append("⚠️  Temperature trending upward - monitor cooling system")
        
        # Vibration insights
        if vib_change > 10:
            insights.append("⚡ Sharp increase in vibration - inspect bearings and mounting bolts")
        elif vib_change > 5:
            insights.append("📈 Vibration levels rising - consider lubrication maintenance")
        
        # Pressure insights
        if pres_change < -5:
            insights.append("💧 Pressure dropping - check for leaks in hydraulic/pneumatic system")
        elif pres_change < -2:
            insights.append("📉 Slight pressure decrease - monitor system integrity")
        
        # Uptime insights
        if uptime_change < -3:
            insights.append("⏱️  Uptime declining - equipment reliability decreasing")
        
        # Defect rate insights
        if defect_change > 1:
            insights.append("🎯 Quality issues increasing - correlates with equipment degradation")
        
        # Correlation insights
        if temp_change > 3 and defect_change > 0.5:
            insights.append("🔗 Temperature increase correlates with quality degradation")
        
        if vib_change > 5 and defect_change > 0.5:
            insights.append("🔗 High vibration affecting product quality")
        
        # Overall assessment
        if not insights:
            insights.append("✅ Equipment performing within normal parameters")
        elif len(insights) >= 3:
            insights.insert(0, "🚨 Multiple degradation indicators - recommend comprehensive inspection")
        
        return insights
    
    async def compare_equipment(
        self,
        equipment_ids: List[str],
        metric: str = "uptime"
    ) -> Dict[str, Any]:
        """
        Compare multiple equipment units
        
        Args:
            equipment_ids: List of equipment IDs to compare
            metric: Metric to compare (uptime, temperature, defect_rate, etc.)
            
        Returns:
            Comparative analysis results
        """
        logger.info(f"Comparing {len(equipment_ids)} equipment units on {metric}")
        
        # Generate mock comparison data
        import numpy as np
        
        comparison_data = {}
        for eq_id in equipment_ids:
            if metric == "uptime":
                value = np.random.uniform(85, 95)
                unit = "%"
            elif metric == "temperature":
                value = np.random.uniform(60, 75)
                unit = "°C"
            elif metric == "defect_rate":
                value = np.random.uniform(1, 4)
                unit = "%"
            else:
                value = np.random.uniform(0, 100)
                unit = ""
            
            comparison_data[eq_id] = {
                "value": value,
                "unit": unit
            }
        
        # Find best and worst performers
        values = [d["value"] for d in comparison_data.values()]
        best_idx = np.argmax(values) if metric in ["uptime"] else np.argmin(values)
        worst_idx = np.argmin(values) if metric in ["uptime"] else np.argmax(values)
        
        best_equipment = equipment_ids[best_idx]
        worst_equipment = equipment_ids[worst_idx]
        
        return {
            "comparison_type": "equipment_comparison",
            "metric": metric,
            "equipment_count": len(equipment_ids),
            "comparison_data": comparison_data,
            "summary": {
                "best_performer": best_equipment,
                "worst_performer": worst_equipment,
                "average": np.mean(values),
                "std_deviation": np.std(values)
            },
            "recommendation": f"Focus maintenance efforts on {worst_equipment} which shows lowest {metric}"
        }
    
    async def calculate_kpis(
        self,
        plant_id: str,
        time_period: str = "last_30_days"
    ) -> Dict[str, Any]:
        """
        Calculate key performance indicators for a plant
        
        Args:
            plant_id: Plant identifier
            time_period: Time period for KPI calculation
            
        Returns:
            Dictionary with calculated KPIs
        """
        logger.info(f"Calculating KPIs for {plant_id} ({time_period})")
        
        import numpy as np
        
        # Mock KPI data
        kpis = {
            "overall_equipment_effectiveness": {
                "value": np.random.uniform(75, 85),
                "unit": "%",
                "target": 80.0,
                "status": "On Target"
            },
            "mean_time_between_failures": {
                "value": np.random.uniform(150, 250),
                "unit": "hours",
                "target": 200.0,
                "status": "Above Target"
            },
            "mean_time_to_repair": {
                "value": np.random.uniform(2, 6),
                "unit": "hours",
                "target": 4.0,
                "status": "On Target"
            },
            "first_pass_yield": {
                "value": np.random.uniform(92, 98),
                "unit": "%",
                "target": 95.0,
                "status": "On Target"
            },
            "total_defect_rate": {
                "value": np.random.uniform(1.5, 3.5),
                "unit": "%",
                "target": 2.0,
                "status": "Needs Attention"
            }
        }
        
        return {
            "plant_id": plant_id,
            "time_period": time_period,
            "kpis": kpis,
            "overall_status": "Satisfactory",
            "areas_of_concern": ["Total defect rate above target"],
            "data_source": "Mock Data (Development Mode)"
        }


# ============================================================================
# Node function for LangGraph integration
# ============================================================================

analytics_agent = AnalyticsAgent()


def analytics_agent_node(state: dict) -> dict:
    """LangGraph node for Analytics Agent"""
    import asyncio
    
    logger.info("Executing Analytics Agent node")
    
    try:
        # Run async function in sync context
        loop = asyncio.get_event_loop()
        if loop.is_running():
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as pool:
                analytics_result = pool.submit(
                    asyncio.run,
                    analytics_agent.analyze_performance_trend(
                        state['equipment_id'],
                        'last_30_days'
                    )
                ).result()
        else:
            analytics_result = loop.run_until_complete(
                analytics_agent.analyze_performance_trend(
                    state['equipment_id'],
                    'last_30_days'
                )
            )
        
        state['analytics_insights'] = analytics_result
        
    except Exception as e:
        logger.error(f"Analytics Agent node error: {e}")
        state.setdefault('errors', []).append(f"Analytics Agent: {str(e)}")
        state['analytics_insights'] = {"error": str(e)}
    
    return state


if __name__ == '__main__':
    # Test Analytics Agent
    import asyncio
    
    logging.basicConfig(level=logging.INFO)
    
    agent = AnalyticsAgent()
    
    # Test performance trend analysis
    result = asyncio.run(agent.analyze_performance_trend('CNC-A-102', 'last_30_days'))
    
    print(f"\n📊 Analytics Agent Test Result:")
    print(f"\nCurrent Metrics:")
    for metric, value in result['current_metrics'].items():
        print(f"  {metric}: {value}")
    
    print(f"\nTrends:")
    for metric, trend in result['trends'].items():
        print(f"  {metric}: {trend}")
    
    print(f"\nInsights:")
    for insight in result['insights']:
        print(f"  {insight}")
