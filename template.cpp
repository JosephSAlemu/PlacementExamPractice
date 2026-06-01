#include <iostream>
#include <stdlib.h>
#include <string>
#include <ranges>
#include <string_view>
#include <vector>
#include <charconv>
#include <stdexcept>

template <typename T>
void excepts(std::string& token, T& val)
{
    auto [ptr, ec] = std::from_chars(token.data(), token.data() + token.size(), val);

    if (ec != std::errc{}) 
    {
        std::cout << "Conversion failed!";
        throw std::exception{};
    }
}

template <typename T>
std::vector<T> split(std::string s, const std::string& delimiter) noexcept(false) {
    std::vector<T> tokens{};
    size_t pos{0};
    std::string token{};
    T value{};
    while ((pos = s.find(delimiter)) != std::string::npos) 
    {
        token = s.substr(0, pos);
        excepts(token, value);
        tokens.push_back(value);
        s.erase(0, pos + delimiter.length());
    }
    excepts(s, value);
    tokens.push_back(value);

    return tokens;
}

template <typename T>
void implementation(std::vector<T>& res)
{

}

template <typename T>
void debugger(std::vector<T>& in)
{
    std::cout << "debugging" << std::endl;
    for(auto& i: in)
    {
        std::cout << i << " ";
    }
    std::cout << std::endl;
}

template <typename T>
void printResult(std::vector<T>& in)
{
    for(auto& i: in)
    {
        std::cout << i;
    }
}

int main()
{
    constexpr bool debug = false;
    int inputType;
    int returnType;
    using inT = decltype(inputType);
    using reT = decltype(returnType);
    using string = std::string;

    string input{};
    std::getline(std::cin, input);
    string delimiter{" "};
    std::vector<inT> parsed{split<inT>(input, delimiter)};
    
    if constexpr(debug)
    {
        debugger<inT>(parsed);
    }
    
    std::vector<reT> result;
    implementation<reT>(result);
    printResult(result);
}