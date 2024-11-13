mkdir CercaStringa
cp Cercastringa.py ./CercaStringa
cp requirements.txt ./CercaStringa
cd CercaStringa
virtualenv myenv
source myenv/bin/activate
pip3 install -r requirements.txt