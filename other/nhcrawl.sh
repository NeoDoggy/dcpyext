#!/bin/bash
##### Constants

TITLE="A nhentai crawler"

##### Functions

usage(){
    echo "usage: "
    echo "      -n {booknumber}  [Needed]"
    echo "      -f {start page}  [Customise]"
    echo "      -l {end page}    [Customise]"
}

##### Settings

if [ "$1" == "" ];then
    usage
    exit 1
fi

if [ "$1" == "-f" -o "$1" == "-l" ];then
    echo "no booknumber"
    exit
fi

while [ "$1" != "" ]; do
    case $1 in
        -n | --booknumber )     
            shift
            booknum=$1
            break
            ;;
        -h | --help )           
            usage
            exit
            ;;
        * )                     
            usage
            exit 1
    esac
    shift
done

first=1

while [ "$2" != "" ]; do
    case $2 in
        -f | --first )          
            shift
            first=$2
            break
            ;;
        -l | --last )           
            shift
            last=$2
            last=$(($last+1))
            break
            ;;
    esac
    shift
done

while [ "$3" != "" ]; do
    case $3 in
        -f | --first )          
            shift
            first=$3
            break
            ;;
        -l | --last )           
            shift
            last=$3
            last=$(($last+1))
            break
            ;;
    esac
    shift
done

if [ "$first" == "" ];then
    first=1
fi

if [ "$last" == "" ];then
    last=1000
fi

echo ""
echo "======== Booknumber:$booknum / startpage:$first / endpage:$(($last-1)) ========"
echo ""

##### Main

mkdir ./temphtml/$booknum
wget -O ./temphtml/$booknum/temp.html https://nhentai.net/g/$booknum/
imgname=$(grep -oP 'galleries\/\K\w+' ./temphtml/$booknum/temp.html | head -1)
i=$first
until [ "$expng" == "Not exist" -a "$exjpg" == "Not exist" ]
do
    echo ""
    echo "======== Now page:${i} ========"
    echo ""
    wget -O ./temphtml/$booknum/$i.png https://i.nhentai.net/galleries/$imgname/$i.png
    expng=$(test -s ./temphtml/$booknum/$i.png && echo "exist" || echo "Not exist" )
    if [ "$expng" == "Not exist" ];then
        echo "======== At page ${i} found no png , changing to jpg ========"
        echo ""
        wget -O ./temphtml/$booknum/$i.png https://i.nhentai.net/galleries/$imgname/$i.jpg
        exjpg=$(test -s ./temphtml/$booknum/$i.png && echo "exist" || echo "Not exist" )
        i=$(($i+1))
    else
        echo "======== Page ${i} image grabbing completed ========"
        echo ""
        i=$(($i+1))
    fi
    if [ "$i" == "$last" ];then
        break
    fi
done

i=$(($i-1))
rm ./temphtml/$booknum/temp.html
if [ "$expng" == "Not exist" -a "$exjpg" == "Not exist" ];then
    echo "======== Page $(($i-1)) is the last page, removing needless files ========"
    echo ""
    rm ./temphtml/$booknum/$i.png
else
    echo "======== Page $i is the last page, removing needless files ========"
    echo ""
fi

echo "======== Hentai program done ======="