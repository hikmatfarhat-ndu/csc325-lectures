#include <vector>
#include <string>
#include <sstream>

std::vector<int> convert(std::vector<std::string>& sv) {
	std::vector<int> iv;
	std::vector<std::string>::iterator itr;
	for (itr = sv.begin();itr != sv.end();itr++) {
		iv.push_back(std::stoi(*itr));
	}
	return iv;

}
std::vector<std::string> split(const std::string& s, char delimiter)
{
	std::vector<std::string> tokens;
	std::string token;
	std::istringstream tokenStream(s);
	while (std::getline(tokenStream, token, delimiter))
	{
		tokens.push_back(token);
	}
	return tokens;
}