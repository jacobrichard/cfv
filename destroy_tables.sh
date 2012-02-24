for i in $(sudo -u postgres psql -d chicagofirevideo -c '\dt+' | grep $1 | awk '{print $3}'); do sudo -u postgres psql -d chicagofirevideo -c "drop table $i cascade"; done
