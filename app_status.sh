DJANGO_FCGI=`ps -ef | grep [f]cgi | wc -l`
NGINX_MASTER=`ps -ef | grep [n]gin | grep master | wc -l`
NGINX_WORKER=`ps -ef | grep [n]gin | grep worker | wc -l`
if [ $NGINX_MASTER -gt 0 ]; then 
  STATUS='RUNNING'
else
  STATUS='NOT RUNNING'
fi
MEMCACHE_STATUS=`ps -ef | grep [m]emcached | wc -l`
if [ $MEMCACHE_STATUS -gt 0 ]; then
  MSTATUS='RUNNING'
else
  MSTATUS='NOT RUNNING'
fi
POSTGRES_STATUS=`ps -ef | grep [p]ostgresql | wc -l`
if [ $POSTGRES_STATUS -gt 0 ]; then
  PSTATUS='RUNNING'
else
  PSTATUS='NOT RUNNING'
fi
echo "Django FCGI Processes Running: $DJANGO_FCGI"
echo "NGINX Master Process: $STATUS"
echo "NGINX Worker Processes: $NGINX_WORKER"
echo "MemcacheD Status: $MSTATUS"
echo "Postgresql Status: $PSTATUS"
