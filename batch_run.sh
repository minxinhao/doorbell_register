rm -f *csv
# for nr_thread in 12 24 36 48 60 72 84 96;do
for nr_thread in 24 36 48 60 72 84 96;do
    # for rmda_depth in 1;do
    for rmda_depth in 1 4 8 16 24 32;do
        echo "nr_thread" $nr_thread "rmda_depth" $rmda_depth
        ../run_mxh.sh $nr_thread $rmda_depth
    done
done