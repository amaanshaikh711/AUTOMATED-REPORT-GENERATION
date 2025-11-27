import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QFileDialog, QProgressBar, QTextEdit,
                             QComboBox, QSpinBox, QCheckBox, QGroupBox, QFormLayout)
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt6.QtGui import QFont, QColor, QIcon, QPixmap, QLinearGradient, QPalette
from PyQt6.QtCore import QSize
import json
from data_analyzer import DataAnalyzer
from report_generator import PDFReportGenerator
from datetime import datetime

class ReportGenerationThread(QThread):
    """Background thread for report generation"""
    progress = pyqtSignal(int)
    status = pyqtSignal(str)
    finished = pyqtSignal(bool)
    
    def __init__(self, csv_file, output_pdf, chart_dir):
        super().__init__()
        self.csv_file = csv_file
        self.output_pdf = output_pdf
        self.chart_dir = chart_dir
    
    def run(self):
        try:
            self.status.emit("Initializing data analyzer...")
            self.progress.emit(10)
            
            analyzer = DataAnalyzer(self.csv_file)
            
            self.status.emit("Performing comprehensive analysis...")
            self.progress.emit(20)
            analysis_results = analyzer.perform_analysis()
            
            self.status.emit("Generating visualizations...")
            self.progress.emit(50)
            analyzer.generate_charts(self.chart_dir)
            
            self.status.emit("Creating PDF report...")
            self.progress.emit(75)
            
            report_gen = PDFReportGenerator(self.output_pdf)
            report_gen.add_title_page(
                "Professional Data Analysis Report",
                "Comprehensive Sales & Performance Analysis",
                datetime.now().strftime("%B %d, %Y")
            )
            report_gen.add_executive_summary(analysis_results)
            report_gen.add_sales_analysis(analysis_results)
            report_gen.add_top_products(analysis_results)
            report_gen.add_category_analysis(analysis_results)
            report_gen.add_regional_analysis(analysis_results)
            report_gen.add_customer_analysis(analysis_results)
            report_gen.add_visualizations(self.chart_dir)
            report_gen.add_shipping_analysis(analysis_results)
            report_gen.add_conclusions()
            report_gen.build()
            
            self.status.emit("Report generation completed successfully!")
            self.progress.emit(100)
            self.finished.emit(True)
        except Exception as e:
            self.status.emit(f"Error: {str(e)}")
            self.finished.emit(False)

class ModernButton(QPushButton):
    """Custom modern button with glassmorphic effect"""
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: rgba(52, 152, 219, 0.8);
                color: white;
                border: 2px solid rgba(52, 152, 219, 0.5);
                border-radius: 10px;
                padding: 10px 20px;
                font-weight: bold;
                font-size: 12px;
                backdrop-filter: blur(10px);
            }
            QPushButton:hover {
                background-color: rgba(41, 128, 185, 0.9);
                border: 2px solid rgba(41, 128, 185, 0.7);
            }
            QPushButton:pressed {
                background-color: rgba(30, 100, 150, 1);
            }
        """)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

class GlassmorphicFrame(QWidget):
    """Glassmorphic container widget"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QWidget {
                background-color: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 15px;
                padding: 20px;
            }
        """)

class InsightifyApp(QMainWindow):
    """Main Application Window - Professional Report Generator"""
    
    def __init__(self):
        super().__init__()
        self.csv_file = None
        self.output_pdf = None
        self.chart_dir = "charts"
        self.init_ui()
        self.apply_theme()
    
    def init_ui(self):
        """Initialize user interface"""
        self.setWindowTitle("Insightify - Professional Report Generator")
        self.setGeometry(100, 100, 1000, 700)
        self.setMinimumSize(900, 600)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
        # Header
        header_layout = QHBoxLayout()
        title_label = QLabel("📊 Insightify")
        title_font = QFont("Segoe UI", 28, QFont.Weight.Bold)
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: #2c3e50;")
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        subtitle_label = QLabel("Professional Automated Report Generation System")
        subtitle_font = QFont("Segoe UI", 11)
        subtitle_label.setFont(subtitle_font)
        subtitle_label.setStyleSheet("color: #7f8c8d;")
        header_layout.addWidget(subtitle_label)
        
        main_layout.addLayout(header_layout)
        main_layout.addSpacing(10)
        
        # File Selection Section
        file_frame = GlassmorphicFrame()
        file_layout = QVBoxLayout(file_frame)
        
        file_label = QLabel("📁 Data Source")
        file_label.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        file_label.setStyleSheet("color: #2c3e50;")
        file_layout.addWidget(file_label)
        
        file_button_layout = QHBoxLayout()
        self.file_button = ModernButton("Select CSV File")
        self.file_button.clicked.connect(self.select_file)
        file_button_layout.addWidget(self.file_button)
        
        self.file_label_display = QLabel("No file selected")
        self.file_label_display.setStyleSheet("color: #7f8c8d; font-style: italic;")
        file_button_layout.addWidget(self.file_label_display)
        file_layout.addLayout(file_button_layout)
        
        main_layout.addWidget(file_frame)
        
        # Output Configuration Section
        config_frame = GlassmorphicFrame()
        config_layout = QFormLayout(config_frame)
        
        config_label = QLabel("⚙️ Configuration")
        config_label.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        config_label.setStyleSheet("color: #2c3e50;")
        config_layout.addRow(config_label)
        
        # Output file
        output_label = QLabel("Output PDF File:")
        output_label.setStyleSheet("color: #2c3e50; font-weight: bold;")
        self.output_input = QLabel("report.pdf")
        self.output_input.setStyleSheet("color: #3498db;")
        config_layout.addRow(output_label, self.output_input)
        
        # Chart directory
        chart_label = QLabel("Chart Directory:")
        chart_label.setStyleSheet("color: #2c3e50; font-weight: bold;")
        self.chart_input = QLabel("charts")
        self.chart_input.setStyleSheet("color: #3498db;")
        config_layout.addRow(chart_label, self.chart_input)
        
        main_layout.addWidget(config_frame)
        
        # Progress Section
        progress_frame = GlassmorphicFrame()
        progress_layout = QVBoxLayout(progress_frame)
        
        progress_label = QLabel("📈 Generation Progress")
        progress_label.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        progress_label.setStyleSheet("color: #2c3e50;")
        progress_layout.addWidget(progress_label)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid rgba(52, 152, 219, 0.3);
                border-radius: 8px;
                text-align: center;
                background-color: rgba(236, 240, 241, 0.5);
            }
            QProgressBar::chunk {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3498db, stop:1 #2980b9);
                border-radius: 6px;
            }
        """)
        progress_layout.addWidget(self.progress_bar)
        
        self.status_label = QLabel("Ready to generate report")
        self.status_label.setStyleSheet("color: #27ae60; font-weight: bold;")
        progress_layout.addWidget(self.status_label)
        
        main_layout.addWidget(progress_frame)
        
        # Action Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        self.generate_button = ModernButton("🚀 Generate Report")
        self.generate_button.setMinimumWidth(200)
        self.generate_button.clicked.connect(self.generate_report)
        button_layout.addWidget(self.generate_button)
        
        self.open_button = ModernButton("📂 Open Report")
        self.open_button.setMinimumWidth(200)
        self.open_button.clicked.connect(self.open_report)
        self.open_button.setEnabled(False)
        button_layout.addWidget(self.open_button)
        
        button_layout.addStretch()
        main_layout.addLayout(button_layout)
        
        # Info Section
        info_frame = GlassmorphicFrame()
        info_layout = QVBoxLayout(info_frame)
        
        info_text = QLabel(
            "ℹ️ <b>How to Use:</b><br/>"
            "1. Select a CSV file containing your data<br/>"
            "2. Click 'Generate Report' to start the analysis<br/>"
            "3. Wait for the process to complete<br/>"
            "4. Click 'Open Report' to view the generated PDF<br/><br/>"
            "<b>Features:</b> Comprehensive data analysis, professional visualizations, "
            "3D charts, and formatted PDF reports."
        )
        info_text.setStyleSheet("color: #34495e; line-height: 1.6;")
        info_text.setWordWrap(True)
        info_layout.addWidget(info_text)
        
        main_layout.addWidget(info_frame)
        main_layout.addStretch()
    
    def apply_theme(self):
        """Apply modern glassmorphic theme"""
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #ecf0f1, stop:1 #bdc3c7);
            }
            QLabel {
                color: #2c3e50;
            }
        """)
    
    def select_file(self):
        """Select CSV file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV File", "", "CSV Files (*.csv);;All Files (*)"
        )
        if file_path:
            self.csv_file = file_path
            file_name = os.path.basename(file_path)
            self.file_label_display.setText(f"✓ {file_name}")
            self.file_label_display.setStyleSheet("color: #27ae60; font-weight: bold;")
            self.status_label.setText("File selected. Ready to generate report.")
            self.status_label.setStyleSheet("color: #27ae60; font-weight: bold;")
    
    def generate_report(self):
        """Generate report in background thread"""
        if not self.csv_file:
            self.status_label.setText("❌ Please select a CSV file first!")
            self.status_label.setStyleSheet("color: #e74c3c; font-weight: bold;")
            return
        
        # Disable button during generation
        self.generate_button.setEnabled(False)
        self.file_button.setEnabled(False)
        
        # Set output paths
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.output_pdf = f"report_{timestamp}.pdf"
        self.chart_dir = f"charts_{timestamp}"
        
        self.output_input.setText(self.output_pdf)
        self.chart_input.setText(self.chart_dir)
        
        # Create and start thread
        self.thread = ReportGenerationThread(self.csv_file, self.output_pdf, self.chart_dir)
        self.thread.progress.connect(self.update_progress)
        self.thread.status.connect(self.update_status)
        self.thread.finished.connect(self.on_generation_finished)
        self.thread.start()
    
    def update_progress(self, value):
        """Update progress bar"""
        self.progress_bar.setValue(value)
    
    def update_status(self, message):
        """Update status label"""
        self.status_label.setText(message)
        self.status_label.setStyleSheet("color: #3498db; font-weight: bold;")
    
    def on_generation_finished(self, success):
        """Handle generation completion"""
        self.generate_button.setEnabled(True)
        self.file_button.setEnabled(True)
        
        if success:
            self.status_label.setText(f"✓ Report generated successfully: {self.output_pdf}")
            self.status_label.setStyleSheet("color: #27ae60; font-weight: bold;")
            self.open_button.setEnabled(True)
        else:
            self.status_label.setText("❌ Report generation failed!")
            self.status_label.setStyleSheet("color: #e74c3c; font-weight: bold;")
    
    def open_report(self):
        """Open generated PDF report"""
        if self.output_pdf and os.path.exists(self.output_pdf):
            os.startfile(self.output_pdf)
        else:
            self.status_label.setText("❌ Report file not found!")
            self.status_label.setStyleSheet("color: #e74c3c; font-weight: bold;")

def main():
    app = QApplication(sys.argv)
    window = InsightifyApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
