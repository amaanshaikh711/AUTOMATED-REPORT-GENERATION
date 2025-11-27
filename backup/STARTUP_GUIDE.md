# Insightify - Startup Guide

## 🚀 Quick Start (5 Minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application

#### Option A: Web Interface (Recommended)
**Windows:**
```bash
run_web.bat
```

**Linux/Mac:**
```bash
python web_server.py
```

Then open your browser to: `http://localhost:8000`

#### Option B: Desktop Application
**Windows:**
```bash
run_gui.bat
```

**Linux/Mac:**
```bash
bash run_gui.sh
```

#### Option C: Command Line
```bash
python example_usage.py
```

---

## 📊 Using the Web Interface

### 1. **Upload Your CSV File**
   - Click the upload area or drag & drop your CSV file
   - File must have headers in the first row
   - Supports files up to 500MB

### 2. **Configure Report Settings**
   - Enter custom report title
   - Enter custom report subtitle
   - Choose visualization options
   - Select analysis parameters

### 3. **Generate Report**
   - Click "Generate Report" button
   - Monitor progress in real-time
   - Wait for analysis to complete (typically 2-5 minutes for 100K rows)

### 4. **View Results**
   - Click "Open Report" to view the PDF
   - Report includes:
     - Professional cover page with Insightify branding
     - Executive summary
     - Detailed analysis sections
     - 10+ professional visualizations
     - Conclusions and recommendations

---

## 📁 Project Structure

```
Insightify/
├── index.html                 # Web interface
├── styles.css                 # Professional styling
├── app.js                      # Frontend JavaScript
├── data_analyzer.py            # Data analysis engine
├── report_generator.py         # PDF report generation
├── ui_application.py           # Desktop GUI (PyQt6)
├── web_server.py              # Web server
├── example_usage.py           # Command-line example
├── run_web.bat                # Web launcher (Windows)
├── run_gui.bat                # GUI launcher (Windows)
├── run_gui.sh                 # GUI launcher (Linux/Mac)
├── requirements.txt           # Python dependencies
├── train.csv                  # Sample dataset
├── PROFESSIONAL_GUIDE.md      # Comprehensive documentation
└── STARTUP_GUIDE.md           # This file
```

---

## 🔧 System Requirements

### Minimum Requirements
- **Python:** 3.8 or higher
- **RAM:** 2GB minimum (4GB recommended)
- **Disk Space:** 500MB for application + space for reports
- **OS:** Windows, Linux, or macOS

### Recommended Requirements
- **Python:** 3.10 or higher
- **RAM:** 8GB or more
- **Disk Space:** 2GB or more
- **Processor:** Multi-core processor for faster analysis

---

## 📦 Dependencies

### Core Libraries
```
pandas>=1.3.0          # Data processing
numpy>=1.21.0          # Numerical operations
matplotlib>=3.4.0      # Visualization
seaborn>=0.11.0        # Statistical graphics
reportlab>=3.6.0       # PDF generation
PyQt6>=6.0.0          # Desktop GUI (optional)
```

### Installation
```bash
pip install -r requirements.txt
```

---

## 📊 Sample Data Format

### Required CSV Structure
Your CSV file should have the following columns:

```
Order ID, Order Date, Ship Date, Ship Mode, Customer ID, Customer Name, 
Segment, Country, City, State, Postal Code, Region, Product ID, Category, 
Sub-Category, Product Name, Sales, Quantity, Discount, Profit
```

### Example Data
```csv
Order ID,Order Date,Ship Date,Ship Mode,Customer ID,Customer Name,Segment,Country,City,State,Postal Code,Region,Product ID,Category,Sub-Category,Product Name,Sales,Quantity,Discount,Profit
CA-2016-152156,11/8/2016,11/11/2016,Second Class,CG-12520,Claire Gute,Consumer,United States,Henderson,Kentucky,42420,South,FUR-BO-10001798,Furniture,Bookcases,Bush Somerset Collection Bookcase,261.96,2,0,41.9136
```

### Supported Data Types
- **Numeric:** Sales, Quantity, Discount, Profit
- **Categorical:** Category, Segment, Region, Ship Mode
- **Temporal:** Order Date, Ship Date
- **Text:** Customer Name, Product Name, City, State

---

## 🎯 Common Use Cases

### 1. Sales Analysis
```
Input: Monthly sales data
Output: Sales trends, top products, regional performance
```

### 2. Customer Segmentation
```
Input: Customer transaction data
Output: Segment analysis, customer value, purchasing patterns
```

### 3. Regional Performance
```
Input: Geographic sales data
Output: Regional rankings, city/state analysis, market insights
```

### 4. Product Analysis
```
Input: Product sales data
Output: Top/bottom products, category analysis, performance metrics
```

### 5. Shipping Analysis
```
Input: Shipping mode data
Output: Shipping efficiency, cost analysis, delivery patterns
```

---

## 🔍 Troubleshooting

### Issue: "Python not found"
**Solution:**
1. Install Python from https://www.python.org
2. Add Python to PATH during installation
3. Restart your terminal/command prompt

### Issue: "Module not found"
**Solution:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Issue: "Port 8000 already in use"
**Solution:**
```bash
python web_server.py 8001  # Use different port
```

### Issue: "Report generation stuck"
**Solution:**
1. Check CSV file format
2. Ensure headers are in first row
3. Try with smaller dataset first
4. Check available disk space

### Issue: "Out of memory"
**Solution:**
1. Close other applications
2. Use 64-bit Python
3. Process smaller datasets
4. Increase system RAM

---

## 📈 Performance Tips

### For Large Datasets (1M+ rows)
1. Use SSD for faster I/O
2. Close unnecessary applications
3. Increase available RAM
4. Consider processing in batches

### For Faster Report Generation
1. Disable 3D charts if not needed
2. Reduce chart resolution
3. Use faster storage (SSD)
4. Close other applications

### For Better Visualizations
1. Increase chart DPI (default: 300)
2. Use larger figure sizes
3. Enable all visualization options
4. Use high-resolution display

---

## 🔐 Data Security

### Local Processing
- ✓ All data stays on your machine
- ✓ No cloud uploads
- ✓ No external API calls
- ✓ Secure file handling

### Report Security
- ✓ Confidential marking on reports
- ✓ Professional footer with branding
- ✓ Secure PDF generation
- ✓ Local file storage

---

## 📞 Support

### Getting Help
1. Check PROFESSIONAL_GUIDE.md for detailed documentation
2. Review example_usage.py for code examples
3. Check troubleshooting section above
4. Contact support@insightify.com

### Reporting Issues
Include:
- Python version
- Operating system
- Error message
- Sample CSV file (if possible)
- Steps to reproduce

---

## 🎓 Learning Resources

### Getting Started
1. Run with sample data (train.csv)
2. Review generated reports
3. Explore different datasets
4. Customize settings

### Advanced Usage
1. Modify analysis parameters
2. Create custom visualizations
3. Integrate with other tools
4. Automate report generation

### Code Examples
```python
# Basic usage
from data_analyzer import DataAnalyzer
from report_generator import PDFReportGenerator

# Load and analyze data
analyzer = DataAnalyzer('data.csv')
results = analyzer.perform_analysis()
analyzer.generate_charts('charts')

# Generate report
report = PDFReportGenerator('report.pdf')
report.add_title_page('Title', 'Subtitle', '2024-01-01')
report.add_executive_summary(results)
report.add_sales_analysis(results)
report.build()
```

---

## 🚀 Next Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   run_web.bat  # Windows
   # or
   python web_server.py  # Linux/Mac
   ```

3. **Upload Your Data**
   - Prepare your CSV file
   - Upload through web interface

4. **Generate Report**
   - Click "Generate Report"
   - Wait for completion

5. **Review Results**
   - Open generated PDF
   - Share with stakeholders

---

## 📝 Version Information

- **Insightify Version:** 1.0
- **Release Date:** 2024
- **Status:** Production Ready
- **License:** Professional Use

---

## 🙏 Thank You

Thank you for using Insightify! We're committed to providing the best data analysis and reporting experience.

**Transform Your Data Into Actionable Insights**

---

*For more information, visit: www.insightify.com*
*Email: info@insightify.com*
*Support: support@insightify.com*
