#include<iostream>
#include<string>
#include<unordered_map>
using namespace std;

int main()
{
	int array[8] = {2,9,10,3,4,2,4,9};
	unordered_map<int,int> umap;
	unordered_map<string,string> umaptest = {
	{"Name", "Ravi Kiran"}, 
	{"University"," USC"}
	};

	for (const auto& n : umaptest) {
		cout << "Key:[" << n.first << "] value[" << n.second << "]"<< endl;
	}

//Using array to implement unordered_map for now. Need to replace with linkedlist 
//traversal later	
	for (int i = 0; i < 8 ; i++)
	{
		auto search = umap.find(array[i]);
		if(search == umap.end()) {
			umap.insert( {{array[i],1}} );
		}
		else {
			cout << array[i] << " occured twice" << endl;
		}
	}

	 for (const auto& n : umap) {
                cout << "Key:[" << n.first << "] value[" << n.second << "]"<< endl;
        }
 
	return 0;
}
