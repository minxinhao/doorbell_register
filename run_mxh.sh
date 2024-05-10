# export TEST_RDMA_CONF=./test_rdma.json
# export SMART_CONFIG_PATH=./smart_config.json
if [ "$1" = "server" ]; then
    # server
    LD_PRELOAD=libmlx5.so ./test_rdma
else
    # test_rdma [nr_thread] [outstanding_work_request_per_thread]
    LD_PRELOAD=libmlx5.so ./test_rdma $1 $2
fi