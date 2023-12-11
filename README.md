# NBA Sports Betting Using Machine Learning 🏀

A machine learning AI used to predict the winners and under/overs of NBA games. Takes all team data from the 2007-08 season to current season, matched with odds of those games, using a neural network to predict winning bets for today's games. Achieves ~69% accuracy on money lines and ~55% on under/overs. Outputs expected value for teams money lines to provide better insight. The fraction of your bankroll to bet based on the Kelly Criterion is also outputted. Note that a popular, less risky approach is to bet 50% of the stake recommended by the Kelly Criterion.

The project has been updated to send an email attachment of todays picks that meet the confidence criteria

## Packages Used

Use Python 3.11. In particular the packages/libraries used are...

- Tensorflow - Machine learning library
- XGBoost - Gradient boosting framework
- Numpy - Package for scientific computing in Python
- Pandas - Data manipulation and analysis
- Colorama - Color text output
- Tqdm - Progress bars
- Requests - Http library
- Scikit_learn - Machine learning library
- Pillow
- boto3
- python-dotenv

## Usage

Make sure all packages above are installed.

```bash
cd nba-ml-ou-picker
pip3 install -r requirements.txt
python3 main.py -xgb -odds=caesars -kc
```

## Get new data and training models

```bash
cd Scripts && python3 process_and_train.py
```
