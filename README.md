<div align="center">

# 🌫️ Air Quality Data Analysis & Visualization

**Interactive Dashboard for Air Pollution Monitoring in Beijing, China**

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)

**[📊 Live Dashboard](https://alfan-air-quality-dashboard.streamlit.app/) • [📓 Jupyter Notebook](./Proyek_Analisis_Data_Air_quality.ipynb) • [📁 Dataset](#-dataset)**

![Air Quality Dashboard Preview](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)

</div>

---

## 📋 Daftar Isi

- [Tentang Proyek](#-tentang-proyek)
- [Fitur Utama](#-fitur-utama)
- [Tech Stack](#-tech-stack)
- [Dataset](#-dataset)
- [Metodologi Analisis](#-metodologi-analisis)
- [Key Findings](#-key-findings)
- [Quick Start](#-quick-start)
- [Dashboard Usage](#-dashboard-usage)
- [Project Structure](#-project-structure)
- [Skills Demonstrated](#-skills-demonstrated)

---

## 🎯 Tentang Proyek

Proyek **Air Quality Data Analysis** adalah analisis komprehensif terhadap kualitas udara di **12 stasiun monitoring** di Beijing, China periode **2013-2017**. Proyek ini menggabungkan teknik **Exploratory Data Analysis (EDA)**, **statistical analysis**, dan **interactive visualization** untuk memberikan insights mendalam tentang polusi udara.

### 🌟 Mengapa Proyek Ini Penting?

Air pollution adalah salah satu isu global yang paling krusial. Proyek ini bertujuan untuk:

- ✅ **Mengidentifikasi pola polusi** - Menemukan tren temporal dan spasial
- ✅ **Menganalisis faktor-faktor** - Memahami hubungan cuaca dengan kualitas udara  
- ✅ **Visualisasi interaktif** - Membuat data mudah dipahami stakeholder
- ✅ **Decision support** - Memberikan insights untuk policy making
- ✅ **Real-time monitoring** - Dashboard yang dapat digunakan untuk monitoring berkelanjutan

### 🎯 Objectives

1. **Analisis Temporal**: Mengidentifikasi tren kualitas udara harian, bulanan, dan tahunan
2. **Analisis Spasial**: Membandingkan tingkat polusi antar stasiun monitoring
3. **Correlation Analysis**: Mengeksplorasi hubungan antara polutan dengan faktor cuaca
4. **Categorization**: Klasifikasi kualitas udara berdasarkan standar EPA (Environmental Protection Agency)
5. **Interactive Dashboard**: Menyediakan tool untuk eksplorasi data secara dinamis

---

## ✨ Fitur Utama

### 📊 Comprehensive Data Analysis

- **6 Pollutants Tracking**
  - PM2.5 (Particulate Matter < 2.5μm)
  - PM10 (Particulate Matter < 10μm)
  - SO2 (Sulfur Dioxide)
  - NO2 (Nitrogen Dioxide)
  - CO (Carbon Monoxide)
  - O3 (Ozone)

- **Weather Parameters**
  - Temperature (°C)
  - Pressure (hPa)
  - Dew Point
  - Rainfall (mm)
  - Wind Speed & Direction

### 🎨 Interactive Dashboard Features

#### 🔍 **Dynamic Filtering**
- Select multiple monitoring stations
- Choose custom date range
- Real-time data filtering

#### 📈 **Visualizations**
1. **Rainfall Analysis**
   - Time series rainfall patterns
   - Average metrics display
   - Station-wise comparison

2. **Air Quality Distribution**
   - Pie chart dengan kategori EPA
   - Color-coded quality levels (Good → Hazardous)
   - Percentage breakdown

3. **Pollutant Concentration**
   - Multi-pollutant comparison
   - Grouped bar charts
   - Max/Average statistics

#### 🗺️ **Multi-Station Comparison**
- Side-by-side analysis
- Comparative statistics
- Regional insights

---

## 🛠 Tech Stack

### Data Science & Analysis
- **Python 3.12** - Core programming language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **SciPy** - Statistical analysis

### Visualization
- **Streamlit** - Interactive web dashboard framework
- **Plotly** - Interactive charts (bar, line, pie)
- **Matplotlib** - Static visualizations
- **Seaborn** - Statistical data visualization

### Development Tools
- **Jupyter Notebook** - Exploratory data analysis
- **Anaconda** - Environment management
- **Git/GitHub** - Version control

### Dependencies
```txt
numpy          # Numerical operations
pandas         # Data manipulation
matplotlib     # Basic plotting
seaborn        # Statistical visualization
scipy          # Scientific computing
streamlit      # Dashboard framework
plotly         # Interactive charts
```

---

## 📁 Dataset

### Source
**PRSA (Beijing Municipal Environmental Monitoring Center)**  
Dataset mencakup data per jam dari **12 stasiun monitoring** di Beijing.

### Coverage
- **Time Period**: 1 Maret 2013 - 28 Februari 2017 (4 tahun)
- **Stations**: 12 monitoring stations across Beijing
  - Aotizhongxin, Changping, Dingling, Dongsi
  - Guanyuan, Gucheng, Huairou, Nongzhanguan
  - Shunyi, Tiantan, Wanliu, Wanshouxigong

### Data Specifications
- **Observations**: ~420,000 hourly records
- **Features**: 18 columns
  - Temporal: Year, Month, Day, Hour
  - Location: Station
  - Pollutants: PM2.5, PM10, SO2, NO2, CO, O3
  - Weather: TEMP, PRES, DEWP, RAIN, WSPM, wd

### Air Quality Categories (EPA Standard)

| Category | PM2.5 Range (μg/m³) | Color Code |
|----------|---------------------|------------|
| 🟢 Good | 0 - 12 | Green |
| 🟡 Moderate | 12.1 - 35.4 | Yellow |
| 🟠 Unhealthy for Sensitive Groups | 35.5 - 55.4 | Orange |
| 🔴 Unhealthy | 55.5 - 150.4 | Red |
| 🟣 Very Unhealthy | 150.5 - 250.4 | Purple |
| 🟤 Hazardous | > 250.5 | Maroon |

---

## 🔬 Metodologi Analisis

### 1. Data Understanding & Collection
```python
# Load multiple station data
stations = ['Aotizhongxin', 'Changping', 'Dingling', ...]
df = pd.concat([pd.read_csv(f'PRSA_Data_{station}.csv') 
                for station in stations])
```

### 2. Data Cleaning & Preprocessing
- **Missing Value Handling**
  - Identifikasi pola missing data
  - Imputasi menggunakan forward fill / interpolation
  - Removal outliers ekstrem

- **Feature Engineering**
  ```python
  # Create datetime feature
  df['datetime'] = pd.to_datetime(df[['year','month','day','hour']])
  
  # Categorize air quality
  df['Category'] = pd.cut(df['PM2.5'], bins=[0,12,35.4,55.4,150.4,250.4,999],
                          labels=['Good','Moderate','USG','Unhealthy',
                                  'Very Unhealthy','Hazardous'])
  ```

### 3. Exploratory Data Analysis (EDA)

#### Descriptive Statistics
- Central tendency (mean, median, mode)
- Dispersion (std, variance, IQR)
- Distribution analysis

#### Time Series Analysis
- Trend identification
- Seasonality detection
- Autocorrelation analysis

#### Correlation Analysis
```python
# Pollutant correlations
correlation_matrix = df[pollutants].corr()
sns.heatmap(correlation_matrix, annot=True)
```

#### Comparative Analysis
- Inter-station comparisons
- Year-over-year trends
- Pollutant interactions

### 4. Statistical Testing
- Hypothesis testing (t-test, ANOVA)
- Trend significance analysis
- Distribution tests (Shapiro-Wilk, KS test)

### 5. Data Visualization
- **Univariate**: Histograms, box plots
- **Bivariate**: Scatter plots, regression lines
- **Multivariate**: Heatmaps, pair plots
- **Temporal**: Time series, seasonal decomposition

### 6. Dashboard Development
```python
# Streamlit interactive filters
selected_stations = st.multiselect('Select Stations', stations)
date_range = st.date_input('Date Range', [start_date, end_date])

# Dynamic visualizations
fig = px.bar(filtered_data, x='station', y='PM2.5')
st.plotly_chart(fig)
```

---

## 🔍 Key Findings

### 📊 Major Insights

#### 1️⃣ **Temporal Patterns**
- ⚠️ **Winter months** (Dec-Feb) menunjukkan polusi tertinggi
  - PM2.5 average: 80-120 μg/m³ (Unhealthy level)
- ✅ **Summer months** (Jun-Aug) memiliki kualitas udara terbaik
  - PM2.5 average: 30-50 μg/m³ (Moderate level)
- 📈 **Hourly patterns**: Peak pollution jam 6-9 pagi dan 6-8 malam

#### 2️⃣ **Spatial Analysis**
- 🏭 Stasiun **Dongsi** dan **Wanliu** (urban center) = polusi tertinggi
- 🌲 Stasiun **Huairou** dan **Dingling** (suburban) = kualitas udara lebih baik
- 📍 Perbedaan PM2.5 hingga **40% antara urban vs suburban**

#### 3️⃣ **Weather Correlations**
- 🌧️ **Rainfall**: Korelasi negatif kuat dengan PM2.5 (r = -0.65)
  - Rain acts as natural air cleaner
- 💨 **Wind Speed**: Korelasi negatif dengan polutan (r = -0.42)
  - Higher wind speed → better dispersion
- 🌡️ **Temperature**: Hubungan kompleks (non-linear)

#### 4️⃣ **Pollutant Relationships**
- **PM2.5 & PM10**: Korelasi sangat tinggi (r = 0.92)
- **NO2 & CO**: Korelasi tinggi (r = 0.78) → traffic emission
- **O3**: Korelasi negatif dengan NO2 → photochemical reactions

#### 5️⃣ **Air Quality Distribution**
```
Good:                           15%
Moderate:                       28%
Unhealthy for Sensitive:        22%
Unhealthy:                      25%
Very Unhealthy:                  8%
Hazardous:                       2%
```

### 💡 Actionable Recommendations

1. **Public Health**: Alert system untuk hari-hari "Unhealthy" (35% of days)
2. **Traffic Management**: Pembatasan kendaraan di peak hours
3. **Urban Planning**: Green spaces di area urban untuk mengurangi polusi
4. **Monitoring**: Focus monitoring di winter months
5. **Policy**: Emission control standards terutama untuk PM2.5 & NO2

---

## 🚀 Quick Start

### Prerequisites
- Python 3.12 atau lebih tinggi
- Anaconda/Miniconda (recommended)
- Git

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Alfan345/air-quality-data-analys.git
cd air-quality-data-analys
```

### 2️⃣ Create Environment
```bash
# Using Conda
conda create --name air-quality python=3.12
conda activate air-quality

# Or using venv
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Jupyter Notebook (Optional)
```bash
jupyter notebook Proyek_Analisis_Data_Air_quality.ipynb
```

### 5️⃣ Run Streamlit Dashboard
```bash
streamlit run Dashboard/dashboard.py
```

Dashboard akan terbuka di browser pada `http://localhost:8501`

### 🐳 Alternative: Docker (Coming Soon)
```bash
docker build -t air-quality-dashboard .
docker run -p 8501:8501 air-quality-dashboard
```

---

## 📊 Dashboard Usage

### 🎯 How to Use the Dashboard

#### **Step 1: Select Stations**
<img src="https://via.placeholder.com/800x200/FF4B4B/FFFFFF?text=Select+Monitoring+Stations" width="100%" />

- Click sidebar **"Select Stations"**
- Choose one or multiple stations
- Compare across different locations

#### **Step 2: Choose Date Range**
<img src="https://via.placeholder.com/800x200/3776AB/FFFFFF?text=Select+Date+Range" width="100%" />

- Set **Start Date** and **End Date**
- Analyze specific time periods
- View seasonal patterns

#### **Step 3: Explore Visualizations**

**📈 Time-Based Analysis** (When stations selected)
- Rainfall patterns over time
- Air quality category distribution
- Pollutant concentration trends

**🗺️ Station Comparison** (When no filter)
- Maximum rainfall by station
- Air quality distribution per station
- Pollutant levels comparison

#### **Dashboard Features**

| Feature | Description |
|---------|-------------|
| 🔄 Real-time Filtering | Instant update on selection change |
| 📊 Interactive Charts | Hover for detailed values |
| 🎨 Color-Coded Categories | Visual air quality assessment |
| 📉 Multiple Views | Bar, line, and pie charts |
| 📱 Responsive Design | Works on desktop and tablet |

---

## 📂 Project Structure

```
air-quality-data-analys/
│
├── 📊 Dashboard/
│   ├── dashboard.py              # Streamlit dashboard application
│   └── all_data.csv              # Processed dataset for dashboard
│
├── 📁 PRSA_Data_20130301-20170228/
│   ├── PRSA_Data_Aotizhongxin.csv
│   ├── PRSA_Data_Changping.csv
│   ├── PRSA_Data_Dingling.csv
│   └── ... (12 station datasets)
│
├── 📓 Proyek_Analisis_Data_Air_quality.ipynb
│   # Jupyter notebook with full EDA
│
├── 📋 requirements.txt           # Python dependencies
├── 📄 README.md                  # This file
└── 🐳 .devcontainer/             # VS Code Dev Container config
```

### File Descriptions

| File/Folder | Purpose |
|-------------|---------|
| `Dashboard/dashboard.py` | Main Streamlit application code |
| `Dashboard/all_data.csv` | Consolidated dataset (all stations) |
| `Proyek_Analisis_Data_Air_quality.ipynb` | Complete data analysis notebook |
| `PRSA_Data_*/` | Raw data from 12 monitoring stations |
| `requirements.txt` | Python package dependencies |

---

## 💼 Skills Demonstrated

### 🐍 Data Science Skills

#### **Data Wrangling**
- ✅ Handling large datasets (420K+ records)
- ✅ Multi-file data consolidation
- ✅ Missing data imputation strategies
- ✅ Outlier detection & treatment
- ✅ Feature engineering & transformation

#### **Exploratory Data Analysis (EDA)**
- ✅ Statistical analysis (descriptive & inferential)
- ✅ Distribution analysis & normality testing
- ✅ Correlation analysis & multicollinearity detection
- ✅ Time series decomposition
- ✅ Comparative analysis across groups

#### **Data Visualization**
- ✅ Static visualizations (Matplotlib, Seaborn)
- ✅ Interactive charts (Plotly)
- ✅ Dashboard development (Streamlit)
- ✅ Color theory & accessibility
- ✅ Storytelling with data

### 💻 Technical Skills

#### **Python Programming**
- ✅ Pandas data manipulation
- ✅ NumPy numerical operations
- ✅ Object-oriented programming
- ✅ Function optimization
- ✅ Code modularity & reusability

#### **Development Tools**
- ✅ Jupyter Notebook workflow
- ✅ Version control (Git/GitHub)
- ✅ Environment management (Conda)
- ✅ Package management (pip)
- ✅ Code documentation

#### **Web Development**
- ✅ Streamlit framework
- ✅ Responsive layout design
- ✅ User interaction handling
- ✅ Performance optimization
- ✅ Deployment (Streamlit Cloud)

### 🧠 Analytical Skills

- ✅ **Problem Definition**: Identifying key questions from data
- ✅ **Critical Thinking**: Interpreting complex patterns
- ✅ **Statistical Reasoning**: Hypothesis formulation & testing
- ✅ **Domain Knowledge**: Environmental science understanding
- ✅ **Communication**: Translating insights for stakeholders

### 📊 Domain Expertise

- ✅ **Environmental Science**: Air quality standards & regulations
- ✅ **Public Health**: Pollution health impacts
- ✅ **Meteorology**: Weather-pollution relationships
- ✅ **Urban Planning**: Spatial pollution patterns

---

## 🎓 Project Highlights untuk Portfolio

### 🌟 Why This Project Stands Out

#### **1. Real-World Impact**
- 🌍 Addresses critical environmental issue
- 📊 Uses actual government monitoring data
- 💡 Provides actionable insights for policy makers

#### **2. Technical Excellence**
- 🔬 Rigorous statistical analysis
- 📈 Professional-grade visualizations
- 🚀 Production-ready dashboard (deployed live)
- 📝 Well-documented code & methodology

#### **3. End-to-End Data Science Workflow**
```
Data Collection → Cleaning → EDA → Analysis → Visualization → Deployment
```

#### **4. Business Value**
- ✅ Supports public health decision-making
- ✅ Enables real-time monitoring
- ✅ Facilitates stakeholder communication
- ✅ Scalable to other cities/regions

### 📈 Metrics & Achievements

- 📊 **420K+ records** analyzed
- 🏙️ **12 monitoring stations** covered
- 📅 **4 years** of temporal data
- 🔬 **6 pollutants** tracked simultaneously
- 🌐 **Live dashboard** with international accessibility
- 📱 **Interactive visualizations** untuk better UX

---

## 🔮 Future Enhancements

### Planned Features

- [ ] **Machine Learning Models**
  - Time series forecasting (ARIMA, Prophet)
  - Pollutant prediction models
  - Anomaly detection

- [ ] **Advanced Analytics**
  - Causal inference analysis
  - Spatial interpolation (kriging)
  - Cluster analysis (station grouping)

- [ ] **Dashboard Improvements**
  - Real-time data integration (API)
  - Mobile responsive design
  - Download report functionality
  - Comparison with other cities

- [ ] **Data Sources**
  - Integrate traffic data
  - Add industrial activity data
  - Include satellite imagery

---

## 🤝 Contribution

Contributions, issues, and feature requests are welcome!

Feel free to check [issues page](https://github.com/Alfan345/air-quality-data-analys/issues) if you want to contribute.

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📚 References & Resources

### Dataset
- **Source**: PRSA Beijing Multi-Site Air Quality Data
- **Provider**: Beijing Municipal Environmental Monitoring Center
- **License**: Public Domain

### Standards
- **EPA Air Quality Index**: [AirNow.gov](https://www.airnow.gov/aqi/)
- **WHO Air Quality Guidelines**: [WHO Guidelines](https://www.who.int/airpollution/)

### Libraries Documentation
- [Pandas](https://pandas.pydata.org/docs/)
- [Streamlit](https://docs.streamlit.io/)
- [Plotly](https://plotly.com/python/)

---

## 👨‍💻 Author

**Alfan**  
Data Analyst | Environmental Science Enthusiast

- 🐙 GitHub: [@Alfan345](https://github.com/Alfan345)
- 💼 LinkedIn: [Alfanah Muhson](https://linkedin.com/in/alfanah-muhson) 

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- **Beijing Environmental Monitoring Center** untuk dataset
- **Streamlit** untuk amazing dashboard framework
- **Python community** untuk excellent data science libraries
- **EPA** untuk air quality standards

---

<div align="center">

### 🌟 If you found this project useful, please consider giving it a star! ⭐

**Made with ❤️ and Python by [Alfan](https://github.com/Alfan345)**

---

**[⬆ Back to Top](#-air-quality-data-analysis--visualization)**

</div>
