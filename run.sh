path=`pwd`
cd `dirname $0`/src

showExp="True"
example=0
output="Fixed-choice MQCC"
while getopts 'e:o:d' OPT; do
    case $OPT in
        d) showExp="False";;
        o) output="$OPTARG";;
        e) example="$OPTARG";;
    esac
done

for last; do true; done

target=$last

file=$path'/'$target # Absolute path of the target file

if [ -f "$target" ]; then
  file=$target
fi


./prepose.sh $file  # Flatten the modules in the program
python3 ./gparser.py preout $showExp $example # Generate expressions and solve the problem