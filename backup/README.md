# 📊 Insightify - Professional Automated Report Generation System

A comprehensive, professional-grade automated report generation system that reads data from CSV files, performs advanced data analysis, and generates beautifully formatted PDF reports with interactive visualizations, 3D charts, and detailed insights.

## ✨ Features

### 🎨 Modern UI
- **Glassmorphic Design**: Modern, visually appealing interface with frosted glass effects
- **Responsive Layout**: Adapts to different screen sizes
- **Real-time Progress**: Live progress tracking during report generation
- **Professional Styling**: Modern color schemes and typography

### 📊 Data Analysis
- **Comprehensive Statistics**: Mean, median, standard deviation, min/max values
- **Sales Analysis**: By category, segment, region, and product
- **Category Analysis**: Sub-category performance and trends
- **Regional Analysis**: Geographic performance metrics
- **Customer Segmentation**: Analysis by customer type
- **Temporal Analysis**: Time-based sales patterns
- **Shipping Analysis**: Shipping mode performance

### 📈 Visualizations
- **10 Professional Charts**:
  1. Sales by Category (Bar Chart)
  2. Sales by Customer Segment (Bar Chart)
  3. Sales by Region (Bar Chart)
  4. Top 10 Products (Horizontal Bar Chart)
  5. Sales Distribution (Histogram)
  6. Category Distribution (Pie Chart)
  7. Regional Performance (Dual Bar Chart)
  8. Customer Segment Distribution (Pie Chart)
  9. **3D Sales Analysis** (3D Scatter Plot)
  10. Shipping Mode Analysis (Dual Chart)

### 📄 PDF Reports
- **Professional Layout**: Multi-page formatted reports
- **Executive Summary**: Key metrics and overview
- **Detailed Analysis**: Comprehensive data breakdowns
- **Data Tables**: Formatted tables with color-coded headers
- **Chart Integration**: All visualizations embedded in PDF
- **Conclusions**: Actionable insights and recommendations

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone or download the project**
```bash
cd "c:\Project 5.0\CodeTech Internship\Task 3 - Insightify"
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 📖 Usage


### Method 1: GUI Application (Recommended)

```bash
python ui_application.py
```

**Steps:**
1. Click "Select CSV File" to choose your data file
2. Click "Generate Report" to start analysis
3. Wait for the progress bar to complete
4. Click "Open Report" to view the generated PDF

### Method 2: Command Line

**Basic usage:**
```bash
python generate_report.py train.csv
```

**With custom output:**
```bash
python generate_report.py train.csv -o my_report.pdf -c my_charts
```

**Verbose output:**
```bash
python generate_report.py train.csv -v
```

**Command line options:**
- `input_file`: Path to CSV file (required)
- `-o, --output`: Output PDF file path (default: report_TIMESTAMP.pdf)
- `-c, --charts`: Charts directory (default: charts)
- `-v, --verbose`: Show detailed output

### Method 3: Python Script

```python
from data_analyzer import DataAnalyzer
from report_generator import PDFReportGenerator

# Analyze data
analyzer = DataAnalyzer('train.csv')
analysis_results = analyzer.perform_analysis()
analyzer.generate_charts('charts')

# Generate report
report = PDFReportGenerator('report.pdf')
report.add_title_page("My Report", "Analysis", "2024-01-01")
report.add_executive_summary(analysis_results)
report.add_sales_analysis(analysis_results)
report.add_visualizations('charts')
report.build()
```

## 📁 Project Structure

```
Task 3 - Insightify/
├── train.csv                 # Sample data file
├── requirements.txt          # Python dependencies
├── data_analyzer.py          # Data analysis engine
├── report_generator.py       # PDF report generator
├── ui_application.py         # GUI application
├── generate_report.py        # CLI script
├── README.md                 # This file
└── charts/                   # Generated charts directory
    ├── 01_sales_by_category.png
    ├── 02_sales_by_segment.png
    ├── 03_sales_by_region.png
    ├── 04_top_products.png
    ├── 05_sales_distribution.png
    ├── 06_category_pie.png
    ├── 07_regional_performance.png
    ├── 08_segment_distribution.png
    ├── 09_3d_sales_analysis.png
    └── 10_shipping_analysis.png
```

## 📊 CSV File Format

The input CSV file should contain the following columns:

```
Row ID, Order ID, Order Date, Ship Date, Ship Mode, Customer ID, 
Customer Name, Segment, Country, City, State, Postal Code, Region, 
Product ID, Category, Sub-Category, Product Name, Sales
```

**Example:**
```csv
1,CA-2017-152156,08/11/2017,11/11/2017,Second Class,CG-12520,Claire Gute,Consumer,United States,Henderson,Kentucky,42420,South,FUR-BO-10001798,Furniture,Bookcases,Bush Somerset Collection Bookcase,261.96
```

## 🎯 Analysis Sections

### 1. Executive Summary
- Total records, sales, and customers
- Average and median transaction values
- Statistical measures

### 2. Sales Analysis
- Sales breakdown by category, segment, and region
- Top and bottom performing products
- Regional sales distribution

### 3. Product Analysis
- Top 10 products by sales
- Bottom 5 products
- Product performance metrics

### 4. Category Analysis
- Category-wise performance
- Top 15 sub-categories
- Category trends

### 5. Regional Analysis
- Top 10 cities by sales
- Top 10 states by sales
- Regional performance comparison

### 6. Customer Analysis
- Customer count by segment
- Average order value by segment
- Segment distribution

### 7. Visualizations
- 10 professional charts
- 3D sales analysis
- Interactive data representations

### 8. Shipping Analysis
- Sales by shipping mode
- Shipping distribution
- Shipping performance metrics

### 9. Conclusions & Recommendations
- Key findings
- Strategic recommendations
- Next steps

## 🎨 Visualization Details

### Chart Types
- **Bar Charts**: Category, segment, and regional comparisons
- **Horizontal Bar Charts**: Top products ranking
- **Histograms**: Sales distribution analysis
- **Pie Charts**: Category and segment distribution
- **3D Scatter Plot**: Multi-dimensional sales analysis
- **Dual Charts**: Comparative analysis

### Color Schemes
- Professional color palettes
- High contrast for readability
- Consistent branding throughout

## 💡 Key Features

### Data Processing
- Automatic data type detection
- Missing value handling
- Date parsing and temporal analysis
- Statistical calculations

### Report Generation
- Multi-page PDF layout
- Professional formatting
- Color-coded tables
- Embedded visualizations
- Automatic pagination

### Performance
- Efficient data processing
- Optimized chart generation
- Fast PDF creation
- Background processing in GUI

## 🔧 Customization

### Modify Analysis
Edit `data_analyzer.py` to add custom analysis:

```python
def _get_custom_analysis(self):
    return {
        'custom_metric': self.df['column'].sum()
    }
```

### Customize Report Layout
Edit `report_generator.py` to change report structure:

```python
def add_custom_section(self, data):
    self.story.append(Paragraph("Custom Section", self.styles['CustomHeading']))
    # Add content
```

### Change UI Theme
Modify the stylesheet in `ui_application.py`:

```python
self.setStyleSheet("""
    QMainWindow {
        background: your_color;
    }
""")
```

## 📋 System Requirements

- **OS**: Windows, macOS, or Linux
- **Python**: 3.8+
- **RAM**: 2GB minimum
- **Disk Space**: 500MB for dependencies

## 🐛 Troubleshooting

### Issue: "Module not found" error
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: GUI doesn't start
**Solution**: Ensure PyQt6 is installed
```bash
pip install PyQt6==6.5.2
```

### Issue: PDF generation fails
**Solution**: Check file permissions and disk space

### Issue: Charts not appearing in PDF
**Solution**: Ensure charts directory exists and contains PNG files

## 📝 Sample Output

The generated report includes:
- Professional title page
- Executive summary with key metrics
- Detailed analysis sections
- 10 high-quality visualizations
- Data tables with statistics
- Conclusions and recommendations
- Professional formatting throughout

## 🎓 Educational Value

This project demonstrates:
- Data analysis with pandas and numpy
- Data visualization with matplotlib and seaborn
- PDF generation with reportlab
- GUI development with PyQt6
- Professional software architecture
- Best practices in data science

## 📄 License

This project is provided for educational purposes.

## 👨‍💼 Author

Developed as part of the CodeTech Internship Program
Task 2: Automated Report Generation

## 🤝 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments
3. Consult the documentation

## 🎉 Features Highlights

✅ **Professional UI** with glassmorphic effects
✅ **Comprehensive Analysis** of sales data
✅ **10 Visualizations** including 3D charts
✅ **Multi-page PDF** reports
✅ **Real-time Progress** tracking
✅ **Command-line Interface** for automation
✅ **Customizable** analysis and reports
✅ **Production-ready** code quality

## 🚀 Future Enhancements

- Interactive dashboard
- Real-time data updates
- Email report delivery
- Custom report templates
- Advanced predictive analytics
- Machine learning insights
- Database integration
- API endpoints

---

**Insightify** - Transform Your Data Into Insights! 📊✨
