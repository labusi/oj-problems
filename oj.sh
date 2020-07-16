# !/bin/bash

if [ $# -lt 1 ]
then
    echo "ERROR：---必须指定题目ID！---"
else
    FILE_NAME="./poj/cpp/$1.cpp"
    echo "#include<iostream>
using namespace std;

int main(int argc, char** argv){

  return 0;
}	 
" > ${FILE_NAME}
    echo "All Done, enjoy!"
fi

emacs -nw ${FILE_NAME}
