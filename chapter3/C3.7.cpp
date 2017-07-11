#include<iostream>
#include<queue>
#include<ctime>
using namespace std;

class animal
{
	private:
	queue<time_t> dog_queue;
	queue<time_t> cat_queue;
	public:
	void fill_queue();
	void adopt_animal();
	bool is_cat_available();
	bool is_dog_available();
};

bool animal::is_cat_available()
{
	if (cat_queue.empty())
	{
		return false;
	}
	else
	{
		return true;
	}
}

bool animal::is_dog_available()
{
	if (dog_queue.empty())
        {
                return false;
        }
        else
        {
                return true;
        }

}
void animal::adopt_animal()
{
	string output;
	cout << "Enter \"cat\" or \"dog\" or \"animal\" :";
        cin >> output;
        if (output == "cat")
        {
		if (!is_cat_available())
		{
			cout << "No cats available at present!" << endl;
			return;
		}
		else
		{
			time_t time = cat_queue.front();
			cat_queue.pop();
			cout << "cat " << time << " is adapted" << endl;
		}
        }
        else if (output == "dog")
        {
		if (!is_dog_available())
                {
                        cout << "No dogs available at present!" << endl;
                        return;
                }
                else
                {
                        time_t time = dog_queue.front();
                        dog_queue.pop();
                        cout << "dog " << time << " is adapted" << endl;
                }

        }
        else if (output == "animal")
        {
		if (is_dog_available() && is_cat_available())
		{
			time_t cat_time =  cat_queue.front();
			time_t dog_time =  dog_queue.front();
			if (cat_time < dog_time)
			{
				cat_queue.pop();
                        	cout << "cat " << cat_time << " is adapted" << endl;
			}
			else
			{
				dog_queue.pop();
				cout << "dog " << dog_time << " is adapted" << endl;
			}
		}
		else if (is_dog_available())
		{
			time_t time = dog_queue.front();
                        dog_queue.pop();
                        cout << "dog " << time << " is adapted" << endl;
		}
		else if (is_cat_available())
		{
			time_t time = cat_queue.front();
                        cat_queue.pop();
                        cout << "cat " << time << " is adapted" << endl;
		}
		else
		{
			cout << "No animals available to adapt at present" << endl;
		}

        }

}

void animal::fill_queue()
{
	int count;
        string input;
        cout << "Enter number of animals :";
        cin >> count;
        for (int i = 0; i < count; i++)
        {
                cout << "Please enter \"cat\" or \"dog\" :" << endl;
                cin >> input;
                if (input == "cat")
                {
                        cat_queue.push(time(0));
                }
                else if (input == "dog")
                {
                        dog_queue.push(time(0));
                }
                else
                {
                        cout << "Invalid input string";
                }
        }	
}

int main()
{
	animal a;
	a.fill_queue();
	a.adopt_animal();
	return 0;
}
