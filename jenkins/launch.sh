case $1 in
    lint)
        find . -type f -name '*.py' -exec python3 -m $2 {} \;
        ;;
    *)
        echo -n "UNKNOWN"
        ;;
esac
