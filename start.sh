if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/sarthakkale16/V6.git /V6
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Auto-Filter-V5
fi
cd /V6
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
https://github.com/sarthakkale16/V6
