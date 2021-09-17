# Archive
# Valable quand on déploie avec un Dockerfile (à la place du heroku.yml)

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
sudo heroku container:push web

echo -e "\n"
echo "--------------------------------"
echo "deploy script --> release app..."
echo "--------------------------------"
heroku container:release web
