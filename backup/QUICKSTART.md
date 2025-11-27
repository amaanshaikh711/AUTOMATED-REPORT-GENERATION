# 🚀 Quick Start Guide - Insightify

Get up and running with Insightify in 5 minutes!

## Step 1: Install Dependencies (2 minutes)

Open Command Prompt and run:

```bash
cd "c:\Project 5.0\CodeTech Internship\Task 3 - Insightify"
pip install -r requirements.txt
```

## Step 2: Choose Your Method

### Option A: GUI Application (Easiest) ⭐

```bash
python ui_application.py
```

**Then:**
1. Click "Select CSV File"
2. Choose `train.csv`
3. Click "Generate Report"
4. Wait for completion
5. Click "Open Report"

### Option B: Command Line

```bash
python generate_report.py train.csv
```

The report will be saved as `report_TIMESTAMP.pdf`

### Option C: Python Script

```python
from data_analyzer import DataAnalyzer
from report_generator import PDFReportGenerator

analyzer = DataAnalyzer('train.csv')
analysis_results = analyzer.perform_analysis()
analyzer.generate_charts('charts')

report = PDFReportGenerator('report.pdf')
report.add_title_page("My Report", "Analysis", "2024-01-01")
report.add_executive_summary(analysis_results)
report.add_sales_analysis(analysis_results)
report.add_visualizations('charts')
report.build()
```

## What You Get

✅ Professional PDF report with:
- Executive summary
- Sales analysis
- Product rankings
- Regional insights
- Customer segmentation
- 10 professional charts
- 3D visualizations
- Detailed conclusions

## File Locations

After generation, you'll find:
- `report_TIMESTAMP.pdf` - Your report
- `charts_TIMESTAMP/` - All visualizations

## Troubleshooting

**Error: "No module named 'pandas'"**
```bash
pip install pandas numpy matplotlib seaborn reportlab fpdf2 PyQt6 Pillow scipy scikit-learn
```

**Error: "CSV file not found"**
- Make sure `train.csv` is in the same directory
- Use full file path if in different location

**GUI won't start**
```bash
pip install PyQt6==6.5.2
```

## Next Steps

1. **Customize Analysis**: Edit `data_analyzer.py`
2. **Modify Report**: Edit `report_generator.py`
3. **Change UI Theme**: Edit `ui_application.py`
4. **Add More Charts**: Add methods to `DataAnalyzer`

## Sample Commands

```bash
# Generate with custom output name
python generate_report.py train.csv -o my_analysis.pdf

# Generate with verbose output
python generate_report.py train.csv -v

# Generate with custom chart directory
python generate_report.py train.csv -c my_charts
```

## Tips

💡 **For Large Files**: Use command line for better performance
💡 **For Automation**: Use `generate_report.py` in scripts
💡 **For Exploration**: Use GUI for interactive analysis
💡 **For Customization**: Edit Python files directly

## Performance

- Small files (< 10MB): ~30 seconds
- Medium files (10-100MB): ~1-2 minutes
- Large files (> 100MB): ~5-10 minutes

## System Requirements

- Python 3.8+
- 2GB RAM
- 500MB disk space
- Windows/Mac/Linux

---

**Ready to generate your first report? Start with Option A above!** 🎉
