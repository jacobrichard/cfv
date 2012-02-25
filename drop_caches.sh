## Drop pagecache, dentries and inodes (to nomalize memory usage)
echo 3 | sudo tee /proc/sys/vm/drop_caches
