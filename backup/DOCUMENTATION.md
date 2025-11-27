# 📚 Insightify - Complete Documentation

## Table of Contents
1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Installation](#installation)
4. [Usage Guide](#usage-guide)
5. [API Reference](#api-reference)
6. [Configuration](#configuration)
7. [Examples](#examples)
8. [Advanced Features](#advanced-features)
9. [Troubleshooting](#troubleshooting)
10. [Performance Optimization](#performance-optimization)

---

## Overview

**Insightify** is a professional-grade automated report generation system designed for data analysts and scientists. It transforms raw CSV data into comprehensive, visually appealing PDF reports with advanced analytics and visualizations.

### Key Capabilities
- **Data Analysis**: Statistical analysis, trend detection, segmentation
- **Visualizations**: 10+ chart types including 3D analysis
- **PDF Reports**: Professional multi-page formatted reports
- **Modern UI**: Glassmorphic design with real-time progress
- **Automation**: CLI and programmatic interfaces

---

## Architecture

### Component Overview

```
┌─────────────────────────────────────────────────────────┐
│                   Insightify System                      │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │     UI       │  │     CLI      │  │   Python     │  │
│  │ Application  │  │   Script     │  │   API        │  │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  │
│         │                 │                 │           │
│         └─────────────────┼──���──────────────┘           │
│                           │                             │
│                    ┌──────▼──────┐                      │
│                    │ Data Analyzer│                      │
│                    │   Engine     │                      │
│                    └──────┬───────┘                      │
│                           │                             │
│         ┌─────────────────┼─────────────────┐           │
│         │                 │                 │           │
│    ┌────▼────┐    ┌──────▼──────┐   ┌─────▼────┐      │
│    │Analysis │    │Visualization│   │ Statistics│      │
│    │ Engine  │    │   Engine     │   │ Engine   │      │
│    └────┬────┘    └──────┬───────┘   └─────┬────┘      │
│         │                 │                 │           │
│         └─────────────────┼─────────────────┘           │
│                           │                             │
│                    ┌──────▼──────┐                      │
│                    │PDF Generator │                      │
│                    │   Engine     │                      │
│                    └──────┬───────┘                      │
│                           │                             │
│                    ┌──────▼──────┐                      │
│                    │ Output Files │                      │
│                    │ (PDF, PNG)   │                      │
│                    └──────────────┘                      │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

### Module Descriptions

#### 1. **data_analyzer.py**
Core analysis engine that processes CSV data.

**Key Classes:**
- `DataAnalyzer`: Main analysis orchestrator

**Key Methods:**
- `perform_analysis()`: Execute all analyses
- `generate_charts()`: Create visualizations
- `_get_basic_stats()`: Calculate statistics
- `_get_sales_analysis()`: Analyze sales patterns
- `_get_category_analysis()`: Category breakdown
- `_get_regional_analysis()`: Geographic analysis
- `_get_customer_analysis()`: Customer segmentation
- `_get_temporal_analysis()`: Time-based patterns
- `_get_shipping_analysis()`: Shipping metrics

#### 2. **report_generator.py**
PDF report creation and formatting.

**Key Classes:**
- `PDFReportGenerator`: Report builder

**Key Methods:**
- `add_title_page()`: Create title page
- `add_executive_summary()`: Add summary section
- `add_sales_analysis()`: Add sales section
- `add_top_products()`: Add product rankings
- `add_category_analysis()`: Add category section
- `add_regional_analysis()`: Add regional section
- `add_customer_analysis()`: Add customer section
- `add_visualizations()`: Embed charts
- `add_shipping_analysis()`: Add shipping section
- `add_conclusions()`: Add conclusions
- `build()`: Generate PDF

#### 3. **ui_application.py**
Modern GUI application with glassmorphic design.

**Key Classes:**
- `InsightifyApp`: Main application window
- `ModernButton`: Custom styled button
- `GlassmorphicFrame`: Container widget
- `ReportGenerationThread`: Background processing

#### 4. **generate_report.py**
Command-line interface for automation.

**Features:**
- Argument parsing
- Progress reporting
- Verbose output
- Error handling

---

## Installation

### System Requirements
- Python 3.8 or higher
- 2GB RAM minimum
- 500MB disk space
- Windows, macOS, or Linux

### Step-by-Step Installation

1. **Navigate to project directory**
```bash
cd "c:\Project 5.0\CodeTech Internship\Task 3 - Insightify"
```

2. **Create virtual environment (optional but recommended)**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Verify installation**
```bash
python -c "import pandas, matplotlib, reportlab; print('✓ All dependencies installed')"
```

---

## Usage Guide

### Method 1: GUI Application

**Start the application:**
```bash
python ui_application.py
```

**Interface Elements:**
- **File Selection**: Choose CSV file
- **Progress Bar**: Real-time progress tracking
- **Status Display**: Current operation status
- **Generate Button**: Start report generation
- **Open Button**: View generated report

**Workflow:**
1. Click "Select CSV File"
2. Choose your data file
3. Click "Generate Report"
4. Wait for completion
5. Click "Open Report"

### Method 2: Command Line

**Basic usage:**
```bash
python generate_report.py train.csv
```

**With options:**
```bash
python generate_report.py train.csv -o my_report.pdf -c my_charts -v
```

**Options:**
- `input_file`: CSV file path (required)
- `-o, --output`: Output PDF path
- `-c, --charts`: Charts directory
- `-v, --verbose`: Detailed output

### Method 3: Python API

**Basic example:**
```python
from data_analyzer import DataAnalyzer
from report_generator import PDFReportGenerator

# Analyze
analyzer = DataAnalyzer('train.csv')
results = analyzer.perform_analysis()
analyzer.generate_charts('charts')

# Generate report
report = PDFReportGenerator('report.pdf')
report.add_title_page("My Report", "Analysis", "2024-01-01")
report.add_executive_summary(results)
report.add_sales_analysis(results)
report.add_visualizations('charts')
report.build()
```

---

## API Reference

### DataAnalyzer Class

```python
class DataAnalyzer:
    def __init__(self, csv_file):
        """Initialize analyzer with CSV file"""
        
    def perform_analysis(self) -> dict:
        """Execute comprehensive analysis"""
        
    def generate_charts(self, output_dir: str) -> str:
        """Generate visualization charts"""
```

**Analysis Results Structure:**
```python
{
    'basic_stats': {
        'total_records': int,
        'total_sales': float,
        'average_sales': float,
        'median_sales': float,
        'std_sales': float,
        'min_sales': float,
        'max_sales': float,
        'unique_customers': int,
        'unique_products': int,
        'unique_orders': int
    },
    'sales_analysis': {
        'total_sales': float,
        'sales_by_category': dict,
        'sales_by_segment': dict,
        'sales_by_region': dict,
        'top_products': dict,
        'bottom_products': dict
    },
    'category_analysis': {...},
    'regional_analysis': {...},
    'customer_analysis': {...},
    'temporal_analysis': {...},
    'shipping_analysis': {...}
}
```

### PDFReportGenerator Class

```python
class PDFReportGenerator:
    def __init__(self, output_file: str):
        """Initialize PDF generator"""
        
    def add_title_page(self, title: str, subtitle: str, date: str):
        """Add title page"""
        
    def add_executive_summary(self, analysis_results: dict):
        """Add executive summary"""
        
    def add_sales_analysis(self, analysis_results: dict):
        """Add sales analysis section"""
        
    def add_visualizations(self, chart_dir: str):
        """Add charts to report"""
        
    def build(self):
        """Generate PDF file"""
```

---

## Configuration

### config.json Structure

```json
{
  "analysis": {
    "enable_temporal_analysis": true,
    "top_n_products": 10,
    "top_n_cities": 10
  },
  "visualizations": {
    "dpi": 300,
    "enable_3d_charts": true
  },
  "pdf_report": {
    "page_size": "A4",
    "title_font_size": 28
  },
  "ui": {
    "theme": "glassmorphic",
    "primary_color": "#3498db"
  }
}
```

### Customization Options

**Analysis Settings:**
- Enable/disable specific analyses
- Adjust top N values
- Set decimal precision

**Visualization Settings:**
- Chart resolution (DPI)
- Figure dimensions
- Color palettes
- Chart types

**PDF Settings:**
- Page size and margins
- Font sizes
- Section inclusion
- Color schemes

**UI Settings:**
- Theme selection
- Color customization
- Window dimensions
- Button styles

---

## Examples

### Example 1: Basic Report
```python
analyzer = DataAnalyzer('data.csv')
results = analyzer.perform_analysis()
analyzer.generate_charts('charts')

report = PDFReportGenerator('report.pdf')
report.add_title_page("Report", "Analysis", "2024-01-01")
report.add_executive_summary(results)
report.add_visualizations('charts')
report.build()
```

### Example 2: Custom Analysis
```python
analyzer = DataAnalyzer('data.csv')
results = analyzer.perform_analysis()

# Access specific results
sales_by_category = results['sales_analysis']['sales_by_category']
top_products = results['sales_analysis']['top_products']

print(f"Total Sales: ${results['basic_stats']['total_sales']:,.2f}")
```

### Example 3: Batch Processing
```python
import os
import glob

for csv_file in glob.glob('data/*.csv'):
    analyzer = DataAnalyzer(csv_file)
    results = analyzer.perform_analysis()
    analyzer.generate_charts(f'charts_{os.path.basename(csv_file)}')
    
    report = PDFReportGenerator(f'report_{os.path.basename(csv_file)}.pdf')
    report.add_title_page("Report", "Analysis", "2024-01-01")
    report.add_executive_summary(results)
    report.add_visualizations(f'charts_{os.path.basename(csv_file)}')
    report.build()
```

---

## Advanced Features

### 1. Custom Analysis Functions

Add custom analysis to `DataAnalyzer`:

```python
def _get_custom_analysis(self):
    return {
        'custom_metric': self.df['column'].sum(),
        'custom_ratio': self.df['col1'].sum() / self.df['col2'].sum()
    }
```

### 2. Custom Chart Types

Add custom charts:

```python
def _chart_custom(self, output_dir):
    fig, ax = plt.subplots(figsize=(10, 6))
    # Your chart code
    plt.savefig(f'{output_dir}/custom_chart.png', dpi=300)
    plt.close()
```

### 3. Report Customization

Modify report sections:

```python
def add_custom_section(self, data):
    self.story.append(Paragraph("Custom Section", self.styles['CustomHeading']))
    # Add custom content
```

### 4. Batch Processing

Process multiple files:

```python
import glob
for file in glob.glob('*.csv'):
    analyzer = DataAnalyzer(file)
    # Process...
```

### 5. Data Filtering

Filter data before analysis:

```python
analyzer = DataAnalyzer('data.csv')
analyzer.df = analyzer.df[analyzer.df['Sales'] > 100]
results = analyzer.perform_analysis()
```

---

## Troubleshooting

### Common Issues

**Issue: "ModuleNotFoundError: No module named 'pandas'"**
```bash
pip install pandas numpy matplotlib seaborn reportlab fpdf2 PyQt6
```

**Issue: "CSV file not found"**
- Verify file path
- Use absolute path if needed
- Check file permissions

**Issue: "GUI won't start"**
```bash
pip install PyQt6==6.5.2
python -m PyQt6.examples.widgets
```

**Issue: "PDF generation fails"**
- Check disk space
- Verify write permissions
- Ensure charts directory exists

**Issue: "Out of memory"**
- Process smaller files
- Increase system RAM
- Use command line instead of GUI

### Debug Mode

Enable verbose output:
```bash
python generate_report.py data.csv -v
```

Check logs:
```bash
tail -f insightify.log
```

---

## Performance Optimization

### Tips for Better Performance

1. **Use Command Line for Large Files**
   - More efficient than GUI
   - Better memory management

2. **Reduce Chart Resolution**
   - Edit config.json: `"dpi": 150`
   - Faster generation, smaller files

3. **Disable Unused Analyses**
   - Edit config.json
   - Disable unnecessary sections

4. **Use Smaller Datasets**
   - Filter data before analysis
   - Process in batches

5. **Optimize System**
   - Close unnecessary applications
   - Ensure sufficient RAM
   - Use SSD for faster I/O

### Performance Benchmarks

| File Size | Processing Time | Output Size |
|-----------|-----------------|-------------|
| 1MB       | ~10 seconds     | 2-3MB       |
| 10MB      | ~30 seconds     | 5-8MB       |
| 50MB      | ~2 minutes      | 15-20MB     |
| 100MB     | ~5 minutes      | 30-40MB     |

---

## Best Practices

1. **Data Preparation**
   - Clean data before analysis
   - Handle missing values
   - Ensure consistent formats

2. **Report Generation**
   - Use meaningful file names
   - Organize output directories
   - Archive old reports

3. **Customization**
   - Document changes
   - Test modifications
   - Keep backups

4. **Automation**
   - Use CLI for scheduled tasks
   - Implement error handling
   - Log all operations

5. **Security**
   - Protect sensitive data
   - Use secure file storage
   - Implement access controls

---

## Support & Resources

- **Documentation**: See README.md
- **Quick Start**: See QUICKSTART.md
- **Examples**: Run example_usage.py
- **Configuration**: Edit config.json

---

## Version History

### v1.0.0 (Current)
- Initial release
- 10 visualization types
- Professional PDF reports
- Modern glassmorphic UI
- CLI and Python API

---

## License

Educational use - CodeTech Internship Program

---

**Insightify** - Transform Your Data Into Insights! 📊✨
