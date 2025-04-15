while true; do
    pid=$(pgrep -f "gnome-system-monitor")
    
    if [ ! -z "$pid" ]; then
        kill -9 $pid
    fi
done