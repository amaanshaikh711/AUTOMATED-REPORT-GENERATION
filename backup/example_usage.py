#!/usr/bin/env python3
"""
Example Usage Script for Insightify
Demonstrates various ways to use the report generation system
"""

import os
import sys
from datetime import datetime
from data_analyzer import DataAnalyzer
from report_generator import PDFReportGenerator

def example_1_basic_report():
    """Example 1: Generate a basic report"""
    print("\n" + "="*70)
    print("EXAMPLE 1: Basic Report Generation")
    print("="*70)
    
    # Check if data file exists
    if not os.path.exists('train.csv'):
        print("❌ train.csv not found!")
        return
    
    print("📊 Analyzing data...")
    analyzer = DataAnalyzer('train.csv')
    analysis_results = analyzer.perform_analysis()
    
    print("📈 Generating charts...")
    analyzer.generate_charts('charts_example1')
    
    print("📄 Creating PDF report...")
    report = PDFReportGenerator('report_example1.pdf')
    report.add_title_page(
        "Sales Analysis Report",
        "Example 1: Basic Report",
        datetime.now().strftime("%B %d, %Y")
    )
    report.add_executive_summary(analysis_results)
    report.add_sales_analysis(analysis_results)
    report.add_visualizations('charts_example1')
    report.build()
    
    print("✅ Report saved as: report_example1.pdf")

def example_2_comprehensive_report():
    """Example 2: Generate a comprehensive report with all sections"""
    print("\n" + "="*70)
    print("EXAMPLE 2: Comprehensive Report Generation")
    print("="*70)
    
    if not os.path.exists('train.csv'):
        print("❌ train.csv not found!")
        return
    
    print("📊 Analyzing data...")
    analyzer = DataAnalyzer('train.csv')
    analysis_results = analyzer.perform_analysis()
    
    print("📈 Generating charts...")
    analyzer.generate_charts('charts_example2')
    
    print("📄 Creating comprehensive PDF report...")
    report = PDFReportGenerator('report_example2_comprehensive.pdf')
    
    # Add all sections
    report.add_title_page(
        "Comprehensive Sales Analysis Report",
        "Example 2: Full Analysis with All Sections",
        datetime.now().strftime("%B %d, %Y")
    )
    
    print("  - Adding executive summary...")
    report.add_executive_summary(analysis_results)
    
    print("  - Adding sales analysis...")
    report.add_sales_analysis(analysis_results)
    
    print("  - Adding product analysis...")
    report.add_top_products(analysis_results)
    
    print("  - Adding category analysis...")
    report.add_category_analysis(analysis_results)
    
    print("  - Adding regional analysis...")
    report.add_regional_analysis(analysis_results)
    
    print("  - Adding customer analysis...")
    report.add_customer_analysis(analysis_results)
    
    print("  - Adding visualizations...")
    report.add_visualizations('charts_example2')
    
    print("  - Adding shipping analysis...")
    report.add_shipping_analysis(analysis_results)
    
    print("  - Adding conclusions...")
    report.add_conclusions()
    
    report.build()
    
    print("✅ Comprehensive report saved as: report_example2_comprehensive.pdf")

def example_3_analysis_only():
    """Example 3: Perform analysis without generating report"""
    print("\n" + "="*70)
    print("EXAMPLE 3: Data Analysis Only (No Report)")
    print("="*70)
    
    if not os.path.exists('train.csv'):
        print("❌ train.csv not found!")
        return
    
    print("📊 Analyzing data...")
    analyzer = DataAnalyzer('train.csv')
    analysis_results = analyzer.perform_analysis()
    
    print("\n📈 Analysis Results:")
    print("-" * 70)
    
    basic_stats = analysis_results['basic_stats']
    print(f"\n📊 Basic Statistics:")
    print(f"   Total Records: {basic_stats['total_records']:,}")
    print(f"   Total Sales: ${basic_stats['total_sales']:,.2f}")
    print(f"   Average Sales: ${basic_stats['average_sales']:,.2f}")
    print(f"   Median Sales: ${basic_stats['median_sales']:,.2f}")
    print(f"   Std Deviation: ${basic_stats['std_sales']:,.2f}")
    print(f"   Min Sales: ${basic_stats['min_sales']:,.2f}")
    print(f"   Max Sales: ${basic_stats['max_sales']:,.2f}")
    print(f"   Unique Customers: {basic_stats['unique_customers']:,}")
    print(f"   Unique Products: {basic_stats['unique_products']:,}")
    print(f"   Unique Orders: {basic_stats['unique_orders']:,}")
    
    sales_data = analysis_results['sales_analysis']
    print(f"\n💰 Sales by Category:")
    for category, sales in sales_data['sales_by_category'].items():
        print(f"   {category}: ${sales:,.2f}")
    
    print(f"\n👥 Sales by Segment:")
    for segment, sales in sales_data['sales_by_segment'].items():
        print(f"   {segment}: ${sales:,.2f}")
    
    print(f"\n🌍 Sales by Region:")
    for region, sales in sales_data['sales_by_region'].items():
        print(f"   {region}: ${sales:,.2f}")
    
    print(f"\n🏆 Top 5 Products:")
    for i, (product, sales) in enumerate(list(sales_data['top_products'].items())[:5], 1):
        print(f"   {i}. {product[:50]}: ${sales:,.2f}")

def example_4_charts_only():
    """Example 4: Generate charts only"""
    print("\n" + "="*70)
    print("EXAMPLE 4: Chart Generation Only")
    print("="*70)
    
    if not os.path.exists('train.csv'):
        print("❌ train.csv not found!")
        return
    
    print("📊 Analyzing data...")
    analyzer = DataAnalyzer('train.csv')
    analyzer.perform_analysis()
    
    print("📈 Generating charts...")
    chart_dir = analyzer.generate_charts('charts_example4')
    
    print(f"\n✅ Charts generated in: {chart_dir}")
    print("\n📊 Generated Charts:")
    charts = sorted([f for f in os.listdir(chart_dir) if f.endswith('.png')])
    for i, chart in enumerate(charts, 1):
        print(f"   {i}. {chart}")

def example_5_custom_analysis():
    """Example 5: Custom analysis with specific focus"""
    print("\n" + "="*70)
    print("EXAMPLE 5: Custom Analysis - Regional Focus")
    print("="*70)
    
    if not os.path.exists('train.csv'):
        print("❌ train.csv not found!")
        return
    
    print("📊 Analyzing data...")
    analyzer = DataAnalyzer('train.csv')
    analysis_results = analyzer.perform_analysis()
    
    print("📈 Generating regional analysis charts...")
    analyzer.generate_charts('charts_example5')
    
    print("📄 Creating regional focus report...")
    report = PDFReportGenerator('report_example5_regional.pdf')
    
    report.add_title_page(
        "Regional Performance Analysis",
        "Example 5: Regional Focus Report",
        datetime.now().strftime("%B %d, %Y")
    )
    
    report.add_executive_summary(analysis_results)
    report.add_regional_analysis(analysis_results)
    report.add_visualizations('charts_example5')
    report.add_conclusions()
    report.build()
    
    print("✅ Regional report saved as: report_example5_regional.pdf")

def main():
    """Run all examples"""
    print("\n" + "="*70)
    print("🚀 INSIGHTIFY - EXAMPLE USAGE DEMONSTRATIONS")
    print("="*70)
    
    examples = [
        ("1", "Basic Report", example_1_basic_report),
        ("2", "Comprehensive Report", example_2_comprehensive_report),
        ("3", "Analysis Only", example_3_analysis_only),
        ("4", "Charts Only", example_4_charts_only),
        ("5", "Regional Focus Report", example_5_custom_analysis),
    ]
    
    print("\nAvailable Examples:")
    for num, name, _ in examples:
        print(f"  {num}. {name}")
    print("  0. Run All Examples")
    print("  Q. Quit")
    
    choice = input("\nSelect example (0-5, Q): ").strip().upper()
    
    if choice == 'Q':
        print("Goodbye!")
        return
    
    if choice == '0':
        for num, name, func in examples:
            try:
                func()
            except Exception as e:
                print(f"❌ Error in example {num}: {str(e)}")
    else:
        for num, name, func in examples:
            if num == choice:
                try:
                    func()
                except Exception as e:
                    print(f"❌ Error: {str(e)}")
                return
        print("❌ Invalid choice!")

if __name__ == '__main__':
    main()
