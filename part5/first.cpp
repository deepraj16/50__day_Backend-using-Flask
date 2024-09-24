#include<iostream>
using namespace std;
int main(){
    string str,str2;
    cin>>str>>str2;
    int j =0;
    for(int i =0;i<str.length(),j<str2.length();i++)
    {
        if(str[i]==str2[j] or (islower(str[i]) and str[i]==tolower(str2[j])))
        {
            j++;
        }
    }
    if(str2.length()==j)
    {
        cout<<"yes"<<endl;
    }
    else cout<<"No"<<endl;
}