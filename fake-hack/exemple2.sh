processus="gnome-system-monitor"

while true; do
    pid=$(pgrep -f $processus)
    
    if [ ! -z "$pid" ]; then
        echo "Processus $processus détecté avec PID $pid. Terminaison..."
        kill -9 $pid
    fi
done
