echo "---------------------------------"
echo "deploy script --> login to heroku"
echo "-------------------------------- "
heroku container:login

echo -e "\n"
echo "------------------------------"
echo "deploy script --> creating app"
echo "------------------------------"
heroku create factures-flow

echo -e "\n"
echo "----------------------------------------------"
echo "deploy script --> pushing container to heroku"
echo "----------------------------------------------"
heroku stack:set container

echo -e "\n"
echo "--------------------------------"
echo "deploy script --> release app..."
echo "--------------------------------"
git push heroku master