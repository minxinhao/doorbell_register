# usage: 
#       ./sync.sh out/in #server
clis=( "192.168.1.51" "192.168.1.52" "192.168.1.53" "192.168.1.10" "192.168.1.11" "192.168.1.12"  "192.168.1.13" "192.168.1.14"  )
if [ "$1" = "out" ]
then
    make -j
    for cli in ${clis[@]:0:$2}
    do 
        echo "cli" $cli
        sshpass -p 'mxh' ssh mxh@$cli "rm -rf server client && mkdir server client"
        sshpass -p 'mxh' scp ./test/test_rdma ../run_mxh.sh libmlx5.so ../config/test_rdma.json ../config/smart_config.json mxh@$cli:/home/mxh/server
        sshpass -p 'mxh' scp ./test/test_rdma ../run_mxh.sh libmlx5.so ../config/test_rdma.json ../config/smart_config.json mxh@$cli:/home/mxh/client
    done
else
    cnt=1
    for cli in ${clis[@]:0:$2}
    do 
        echo "cli" $cli
        # rm -f ./out$cli.txt
        # sshpass -p 'mxh' scp mxh@$cli:/home/mxh/client/out.txt ./out$cli.txt
        ((cnt += 1))
    done
fi