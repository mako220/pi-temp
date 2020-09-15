echo "$(date) @ $(hostname)"
cpu=$(</sys/class/thermal/thermal_zone0/temp)
echo "-------------------------------------------"
echo "GPU => $(/opt/vc/bin/vcgencmd measure_temp)"
echo "CPU => $((cpu/1000))'C"
