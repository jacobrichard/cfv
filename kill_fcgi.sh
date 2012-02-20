ps -ef | grep fcgi | awk '$3 == 1 {print $2}' | xargs kill
