# Market Prophet

## Overview

This project aims to predict stock market trends by combining three key analyses: Technical, Fundamental, and Sentiment. The system employs a holistic approach, utilizing stock market indicators for Technical Analysis, regression models fine-tuned for Fundamental Analysis, and a custom algorithm for normalizing and aggregating results. The inclusion of Sentiment Analysis enhances the predictive power, creating a robust framework for forecasting stock movements.

## Features

- **Technical Analysis:** Incorporates various stock market indicators and metrics for understanding historical price movements and trends.
  
- **Fundamental Analysis:** Utilizes regression models, fine-tuned with historical financial data, to evaluate a company's intrinsic value and growth potential.

- **Sentiment Analysis:** Integrates sentiment analysis on news articles, social media, and financial reports to gauge market sentiment and its impact on stock prices.

- **Normalization Algorithm:** A proprietary algorithm designed from scratch to normalize and aggregate results from both Technical and Fundamental analyses, ensuring a unified and consistent prediction model.

## Requirements

- Python 3.x
- Pandas, NumPy, Scikit-Learn, TensorFlow (for machine learning components)
- Natural Language Toolkit (NLTK) for Sentiment Analysis
- Matplotlib, Seaborn (for visualization)

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/stock-prediction-system.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the main prediction script:

```bash
python predict.py
```

## Contributions

Contributions are welcome! If you have suggestions, find bugs, or want to add new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Acknowledgments

- Special thanks to the open-source community for providing valuable tools and libraries.

Happy forecasting! 📈🚀
