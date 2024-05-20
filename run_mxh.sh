# export TEST_RDMA_CONF=./test_rdma.json
# export SMART_CONFIG_PATH=./smart_config.json
make test_rdma
cp ./test/test_rdma .
if [ "$1" = "server" ]; then
    # server
    LD_PRELOAD=../libmlx5.so ./test/test_rdma
    # LD_PRELOAD=libmlx5.so ./test/test_rdma
    # ./test/test_rdma
else
    # test_rdma [nr_thread] [outstanding_work_request_per_thread]
    # LD_PRELOAD=../libmlx5.so ./test_rdma $1 $2
    LD_PRELOAD=libmlx5.so ./test_rdma $1 $2
    # ./test_rdma $1 $2
fi