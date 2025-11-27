#!/usr/bin/env python3
"""
Insightify - Enhanced Example Usage
Demonstrates how to use Insightify for professional data analysis and report generation
"""

import os
import sys
from datetime import datetime
from data_analyzer import DataAnalyzer
from report_generator import PDFReportGenerator

def print_header():
    """Print application header"""
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║                    INSIGHTIFY v1.0                         ║
    ║     Professional Data Analysis & Report Generation         ║
    ║                                                            ║
    ║  Transform Your Data Into Actionable Insights             ║
    ╚═════════════════════════���══════════════════════════════════╝
    """)

def print_section(title):
    """Print section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

def analyze_and_report(csv_file, output_pdf=None, chart_dir=None):
    """
    Complete workflow: Analyze data and generate professional report
    
    Args:
        csv_file (str): Path to CSV file
        output_pdf (str): Output PDF filename (optional)
        chart_dir (str): Chart directory (optional)
    """
    
    print_header()
    
    # Validate input file
    print_section("Step 1: Validating Input File")
    if not os.path.exists(csv_file):
        print(f"[✗] Error: File '{csv_file}' not found")
        return False
    
    file_size_mb = os.path.getsize(csv_file) / (1024 * 1024)
    print(f"[✓] File found: {csv_file}")
    print(f"[✓] File size: {file_size_mb:.2f} MB")
    
    # Set default output names if not provided
    if output_pdf is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_pdf = f"report_{timestamp}.pdf"
    
    if chart_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        chart_dir = f"charts_{timestamp}"
    
    print(f"[✓] Output PDF: {output_pdf}")
    print(f"[✓] Chart directory: {chart_dir}")
    
    # Load and analyze data
    print_section("Step 2: Loading and Analyzing Data")
    try:
        analyzer = DataAnalyzer(csv_file)
        print(f"[✓] Data loaded successfully")
        print(f"[✓] Dataset size: {len(analyzer.df):,} rows, {len(analyzer.df.columns)} columns")
        
        # Perform analysis
        print("\n[*] Performing comprehensive analysis...")
        analysis_results = analyzer.perform_analysis()
        print("[✓] Analysis completed successfully")
        
        # Display key metrics
        print_section("Key Metrics")
        basic_stats = analysis_results['basic_stats']
        print(f"Total Records:        {basic_stats['total_records']:,}")
        print(f"Total Sales:          ${basic_stats['total_sales']:,.2f}")
        print(f"Average Sales:        ${basic_stats['average_sales']:,.2f}")
        print(f"Median Sales:         ${basic_stats['median_sales']:,.2f}")
        print(f"Min Sales:            ${basic_stats['min_sales']:,.2f}")
        print(f"Max Sales:            ${basic_stats['max_sales']:,.2f}")
        print(f"Unique Customers:     {basic_stats['unique_customers']:,}")
        print(f"Unique Products:      {basic_stats['unique_products']:,}")
        print(f"Unique Orders:        {basic_stats['unique_orders']:,}")
        
    except Exception as e:
        print(f"[✗] Error during analysis: {str(e)}")
        return False
    
    # Generate visualizations
    print_section("Step 3: Generating Visualizations")
    try:
        print("[*] Creating charts and graphs...")
        analyzer.generate_charts(chart_dir)
        print(f"[✓] Visualizations saved to: {chart_dir}")
        
        # List generated charts
        chart_files = sorted([f for f in os.listdir(chart_dir) if f.endswith('.png')])
        print(f"[✓] Generated {len(chart_files)} charts:")
        for i, chart in enumerate(chart_files, 1):
            print(f"    {i}. {chart}")
        
    except Exception as e:
        print(f"[✗] Error generating visualizations: {str(e)}")
        return False
    
    # Generate PDF report
    print_section("Step 4: Generating PDF Report")
    try:
        print("[*] Creating professional PDF report...")
        
        report_gen = PDFReportGenerator(output_pdf)
        
        # Add title page
        print("[*] Adding title page...")
        report_gen.add_title_page(
            "Professional Data Analysis Report",
            "Comprehensive Sales & Performance Analysis",
            datetime.now().strftime("%B %d, %Y")
        )
        
        # Add executive summary
        print("[*] Adding executive summary...")
        report_gen.add_executive_summary(analysis_results)
        
        # Add sales analysis
        print("[*] Adding sales analysis...")
        report_gen.add_sales_analysis(analysis_results)
        
        # Add top products
        print("[*] Adding top products analysis...")
        report_gen.add_top_products(analysis_results)
        
        # Add category analysis
        print("[*] Adding category analysis...")
        report_gen.add_category_analysis(analysis_results)
        
        # Add regional analysis
        print("[*] Adding regional analysis...")
        report_gen.add_regional_analysis(analysis_results)
        
        # Add customer analysis
        print("[*] Adding customer segment analysis...")
        report_gen.add_customer_analysis(analysis_results)
        
        # Add visualizations
        print("[*] Adding visualizations...")
        report_gen.add_visualizations(chart_dir)
        
        # Add shipping analysis
        print("[*] Adding shipping analysis...")
        report_gen.add_shipping_analysis(analysis_results)
        
        # Add conclusions
        print("[*] Adding conclusions and recommendations...")
        report_gen.add_conclusions()
        
        # Build PDF
        print("[*] Building PDF...")
        report_gen.build()
        
        print(f"[✓] Report generated successfully: {output_pdf}")
        
    except Exception as e:
        print(f"[✗] Error generating report: {str(e)}")
        return False
    
    # Summary
    print_section("Generation Complete")
    print(f"[✓] Report: {output_pdf}")
    print(f"[✓] Charts: {chart_dir}/")
    print(f"[✓] Total time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    print_section("Next Steps")
    print("1. Open the generated PDF report")
    print("2. Review the analysis and insights")
    print("3. Share with stakeholders")
    print("4. Use insights for decision-making")
    
    return True

def main():
    """Main entry point"""
    
    # Check command line arguments
    if len(sys.argv) < 2:
        print_header()
        print("Usage: python example_usage_enhanced.py <csv_file> [output_pdf] [chart_dir]")
        print("\nExample:")
        print("  python example_usage_enhanced.py train.csv report.pdf charts/")
        print("\nSupported CSV columns:")
        print("  - Order ID, Order Date, Ship Date, Ship Mode")
        print("  - Customer ID, Customer Name, Segment")
        print("  - Country, City, State, Postal Code, Region")
        print("  - Product ID, Category, Sub-Category, Product Name")
        print("  - Sales, Quantity, Discount, Profit")
        print("\nFor more information, see PROFESSIONAL_GUIDE.md")
        return
    
    csv_file = sys.argv[1]
    output_pdf = sys.argv[2] if len(sys.argv) > 2 else None
    chart_dir = sys.argv[3] if len(sys.argv) > 3 else None
    
    # Run analysis and report generation
    success = analyze_and_report(csv_file, output_pdf, chart_dir)
    
    if success:
        print("\n[✓] All operations completed successfully!")
        sys.exit(0)
    else:
        print("\n[✗] Operation failed!")
        sys.exit(1)

if __name__ == '__main__':
    main()
