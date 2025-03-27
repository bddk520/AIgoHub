# c++容器用法

## set

在 C++ 中，集合（`set`）是一个非常有用的数据结构，它存储的是唯一的元素，且按特定的顺序自动排序。集合通常使用 `std::set` 来实现，`std::set` 是 C++ 标准库提供的一种容器，底层通常使用红黑树或其他平衡树来实现，提供高效的查找、插入和删除操作。

### 基本用法

#### 1. **包含头文件**

要使用 `std::set`，首先需要包含头文件：

```cpp
#include <set>
#include <iostream>
```

#### 2. **声明和初始化**

`std::set` 默认按升序排序元素，也可以指定排序的规则。

```cpp
std::set<int> mySet;  // 创建一个整型集合，默认按升序排序
```

#### 3. **插入元素**

可以使用 `insert()` 方法将元素插入集合。`set` 会自动忽略重复的元素。

```cpp
mySet.insert(10);
mySet.insert(20);
mySet.insert(10);  // 插入重复元素，集合中不会存储重复值
```

#### 4. **遍历集合**

使用范围 `for` 循环可以遍历集合中的元素。

```cpp
for (const auto& elem : mySet) {
    std::cout << elem << " ";
}
std::cout << std::endl;
```

#### 5. **查找元素**

使用 `find()` 方法查找一个元素。如果元素存在，返回指向该元素的迭代器；如果不存在，返回 `end()` 迭代器。

```cpp
auto it = mySet.find(10);
if (it != mySet.end()) {
    std::cout << "Found: " << *it << std::endl;
} else {
    std::cout << "Not Found" << std::endl;
}
```

#### 6. **删除元素**

使用 `erase()` 方法删除指定元素或指定位置的元素。

```cpp
mySet.erase(10);  // 删除元素 10
```

#### 7. **其他常用操作**

* **`size()`** : 获取集合中元素的个数。
* **`empty()`** : 检查集合是否为空。

```cpp
std::cout << "Size: " << mySet.size() << std::endl;
std::cout << "Is empty: " << (mySet.empty() ? "Yes" : "No") << std::endl;
```

### 示例代码：

```cpp
#include <iostream>
#include <set>

int main() {
    std::set<int> mySet;

    // 插入元素
    mySet.insert(5);
    mySet.insert(2);
    mySet.insert(8);
    mySet.insert(2);  // 这个元素不会被插入，重复元素会被忽略

    // 遍历并打印元素
    std::cout << "Set elements: ";
    for (const auto& elem : mySet) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;

    // 查找元素
    auto it = mySet.find(5);
    if (it != mySet.end()) {
        std::cout << "Element 5 found." << std::endl;
    } else {
        std::cout << "Element 5 not found." << std::endl;
    }

    // 删除元素
    mySet.erase(2);  // 删除元素 2

    // 打印删除后的集合
    std::cout << "Set after deletion: ";
    for (const auto& elem : mySet) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;

    // 检查集合大小
    std::cout << "Size of set: " << mySet.size() << std::endl;

    return 0;
}
```

#### 输出：

```
Set elements: 2 5 8 
Element 5 found.
Set after deletion: 5 8 
Size of set: 2
```

### 注意：

1. `std::set` 中的元素是  **唯一的** ，即不会存储重复元素。
2. 默认按 **升序** 排序元素，可以通过指定自定义比较函数来改变排序方式。
3. `std::set` 提供了  **高效的查找、插入和删除操作** ，复杂度通常为 `O(log n)`。

### 使用自定义排序：

如果你希望集合按照降序或其他特定顺序进行排序，可以指定比较函数。例如：

```cpp
std::set<int, std::greater<int>> mySet;  // 降序排列

mySet.insert(10);
mySet.insert(20);
mySet.insert(5);

for (const auto& elem : mySet) {
    std::cout << elem << " ";  // 输出：20 10 5
}
```

通过这些基本操作，你可以在 C++ 中有效地使用集合（`std::set`）。

在 C++ 中，`std::set` 提供了一些非常方便的成员函数和算法来执行集合操作（如求交集、并集等）。这些操作通常可以通过标准库的算法 `std::set_intersection`、`std::set_union`、`std::set_difference` 等来实现。

### 常用集合操作：

* **交集（Intersection）** : 找出两个集合中共同存在的元素。
* **并集（Union）** : 合并两个集合，去除重复元素。
* **差集（Difference）** : 找出第一个集合中存在而第二个集合中不存在的元素。

### 示例代码

```cpp
#include <iostream>
#include <set>
#include <algorithm>  // std::set_intersection, std::set_union, std::set_difference

int main() {
    // 创建两个集合
    std::set<int> set1 = {1, 2, 3, 4, 5};
    std::set<int> set2 = {3, 4, 5, 6, 7};

    // 求交集
    std::set<int> intersectionSet;
    std::set_intersection(set1.begin(), set1.end(), set2.begin(), set2.end(),
                          std::inserter(intersectionSet, intersectionSet.begin()));

    std::cout << "Intersection: ";
    for (const auto& elem : intersectionSet) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;

    // 求并集
    std::set<int> unionSet;
    std::set_union(set1.begin(), set1.end(), set2.begin(), set2.end(),
                   std::inserter(unionSet, unionSet.begin()));

    std::cout << "Union: ";
    for (const auto& elem : unionSet) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;

    // 求差集
    std::set<int> differenceSet;
    std::set_difference(set1.begin(), set1.end(), set2.begin(), set2.end(),
                        std::inserter(differenceSet, differenceSet.begin()));

    std::cout << "Difference (set1 - set2): ";
    for (const auto& elem : differenceSet) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

#### 输出：

```
Intersection: 3 4 5 
Union: 1 2 3 4 5 6 7 
Difference (set1 - set2): 1 2 
```

### 解释：

1. **交集（Intersection）** :

* 使用 `std::set_intersection` 来找到 `set1` 和 `set2` 中共同的元素。这个算法的结果是 `set1` 和 `set2` 的交集，存储在 `intersectionSet` 中。

```cpp
   std::set_intersection(set1.begin(), set1.end(), set2.begin(), set2.end(),
                         std::inserter(intersectionSet, intersectionSet.begin()));
```

1. **并集（Union）** :

* 使用 `std::set_union` 来计算 `set1` 和 `set2` 的并集。该算法会将两个集合的所有元素合并，并且去除重复的元素（因为 `set` 本身只允许唯一元素）。

```cpp
   std::set_union(set1.begin(), set1.end(), set2.begin(), set2.end(),
                  std::inserter(unionSet, unionSet.begin()));
```

1. **差集（Difference）** :

* 使用 `std::set_difference` 来找出 `set1` 中有而 `set2` 中没有的元素（`set1 - set2`）。结果存储在 `differenceSet` 中。

```cpp
   std::set_difference(set1.begin(), set1.end(), set2.begin(), set2.end(),
                       std::inserter(differenceSet, differenceSet.begin()));
```

### 说明：

* **`std::set_intersection`** : 计算两个集合的交集。
* **`std::set_union`** : 计算两个集合的并集。
* **`std::set_difference`** : 计算两个集合的差集（即一个集合中有而另一个集合中没有的元素）。

这些算法要求输入的集合是已经排序的，这也是 `std::set` 容器天然支持这些操作的原因。

### 其他集合操作：

* **对称差集（Symmetric Difference）** : 计算两个集合的对称差集（即两个集合的元素中，只在一个集合中出现的元素）。使用 `std::set_symmetric_difference` 可以实现。

```cpp
  std::set<int> symmetricDifferenceSet;
  std::set_symmetric_difference(set1.begin(), set1.end(), set2.begin(), set2.end(),
                                std::inserter(symmetricDifferenceSet, symmetricDifferenceSet.begin()));
```

这些集合操作非常高效，能够在 `O(n log n)` 的时间复杂度下完成，适用于需要处理大量数据的场景。

## string

在 C++ 中，`std::string` 类是标准库提供的用于处理字符串的类，封装了对字符串的各种操作，提供了更安全和便捷的功能。以下是 `std::string` 类的基本用法和常见操作：

### 1. **包含头文件**

在使用 `std::string` 类之前，需要包含 `<string>` 头文件：

```cpp
#include <string>
```

### 2. **创建和初始化字符串**

可以通过多种方式创建和初始化 `std::string` 对象：

```cpp
#include <iostream>
#include <string>

int main() {
    std::string str1;                      // 默认构造函数，创建一个空字符串
    std::string str2("Hello, World!");     // 使用C风格字符串初始化
    std::string str3(str2);                // 拷贝构造函数
    std::string str4(5, 'A');              // 创建一个包含5个字符 'A' 的字符串

    std::cout << str1 << std::endl;        // 输出: （空行）
    std::cout << str2 << std::endl;        // 输出: Hello, World!
    std::cout << str3 << std::endl;        // 输出: Hello, World!
    std::cout << str4 << std::endl;        // 输出: AAAAA

    return 0;
}
```

### 3. **获取字符串长度**

使用 `length()` 或 `size()` 方法获取字符串的长度，这两个方法功能相同：

```cpp
#include <iostream>
#include <string>

int main() {
    std::string str = "Hello";
    std::cout << "Length: " << str.length() << std::endl; // 输出: Length: 5
    std::cout << "Size: " << str.size() << std::endl;     // 输出: Size: 5

    return 0;
}
```

### 4. **字符串拼接**

可以使用 `+` 运算符或 `append()` 方法进行字符串拼接：

```cpp
#include <iostream>
#include <string>

int main() {
    std::string str1 = "Hello";
    std::string str2 = " World";

    // 使用 + 运算符拼接
    std::string str3 = str1 + str2;
    std::cout << str3 << std::endl; // 输出: Hello World

    // 使用 append() 方法拼接
    str1.append(str2);
    std::cout << str1 << std::endl; // 输出: Hello World

    return 0;
}
```

### 5. **访问和修改字符串中的字符**

可以使用下标运算符 `[]` 或 `at()` 方法访问和修改字符串中的字符：

```cpp
#include <iostream>
#include <string>

int main() {
    std::string str = "Hello";

    // 访问字符
    char ch1 = str[0];       // 'H'
    char ch2 = str.at(1);    // 'e'

    std::cout << ch1 << std::endl; // 输出: H
    std::cout << ch2 << std::endl; // 输出: e

    // 修改字符
    str[0] = 'h';
    str.at(1) = 'a';

    std::cout << str << std::endl; // 输出: hallo

    return 0;
}
```

### 6. **子字符串提取**

使用 `substr()` 方法提取子字符串：

```cpp
#include <iostream>
#include <string>

int main() {
    std::string str = "Hello, World!";
    std::string subStr = str.substr(7, 5); // 从位置7开始，提取5个字符

    std::cout << subStr << std::endl; // 输出: World

    return 0;
}
```

### 7. **查找子字符串**

使用 `find()` 方法查找子字符串的位置：

```cpp
#include <iostream>
#include <string>

int main() {
    std::string str = "Hello, World!";
    size_t pos = str.find("World");

    if (pos != std::string::npos) {
        std::cout << "Found at position: " << pos << std::endl; // 输出: Found at position: 7
    } else {
        std::cout << "Not found" << std::endl;
    }

    return 0;
}
```

### 8. **替换子字符串**

使用 `replace()` 方法替换子字符串：

```cpp
#include <iostream>
#include <string>

int main() {
    std::string str = "Hello, World!";
    str.replace(7, 5, "C++"); // 从位置7开始，替换5个字符为 "C++"

    std::cout << str << std::endl; // 输出: Hello, C++!

    return 0;
}
```

### 9. **字符串比较**

可以使用比较运算符（如 `==`、`!=`、`<`、`>` 等）或 `compare()` 方法进行字符串比较：

```cpp
#include <iostream>
#include <string>

int main() {
    std::string str1 = "Hello";
    std::string str2 = "World";

    // 使用比较运算符
    if (str1 == str2) {
        std::cout << "str1 equals str2" << std::endl;
    } else {
        std::cout << "str1 does not equal str2" << std::endl; // 输出: str1 does not equal str2
    }

    // 使用 compare() 方法
    if (str1.compare(str2) == 0) {
        std::cout << "str1 equals str2" << std::endl;
    } else {
        std::cout << "str1 does not equal str2" << std::endl; // 输出: str1 does not equal str2
    }

    return 0;
}
```

### 10. **转换为 C 风格字符串**

使用 `c_str()` 方法将 `std::string` 转换为 C 风格字符串（以 null 终止的字符数组）：

```cpp
#include <iostream>
#include <string>

int main() {
    std::string str = "Hello, World!";
    const char* cStr = str.c_str();

    std::cout << cStr << std::endl; // 输出: Hello, World!

    return 0;
}
```

## vector

在 C++ 中，`std::vector` 是标准模板库（STL）提供的一个动态数组容器，能够自动管理内存，支持在运行时动态地插入和删除元素。 citeturn0search4

### 1. **引入头文件**

在使用 `std::vector` 之前，需要包含 `<vector>` 头文件：

```cpp
#include <vector>
```

### 2. **创建和初始化 `vector`**

可以通过多种方式创建和初始化 `vector`：

```cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec1;                 // 创建一个空的 vector
    std::vector<int> vec2(10);             // 创建一个包含 10 个默认初始化元素的 vector
    std::vector<int> vec3(5, 100);         // 创建一个包含 5 个值为 100 的元素的 vector
    std::vector<int> vec4 = {1, 2, 3, 4};  // 使用列表初始化 vector

    return 0;
}
```

### 3. **访问和修改元素**

可以使用下标运算符 `[]` 或 `at()` 方法访问和修改 `vector` 中的元素：

```cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec = {10, 20, 30, 40};

    // 使用下标访问元素
    std::cout << vec[0] << std::endl;  // 输出: 10

    // 使用 at() 方法访问元素
    std::cout << vec.at(1) << std::endl;  // 输出: 20

    // 修改元素
    vec[2] = 100;
    std::cout << vec[2] << std::endl;  // 输出: 100

    return 0;
}
```

**注意：** `at()` 方法在访问越界时会抛出 `std::out_of_range` 异常，而使用 `[]` 运算符时，行为未定义。

### 4. **添加和删除元素**

`std::vector` 提供了多种方法来添加和删除元素：

* **`push_back()`** ：在末尾添加元素。
* **`pop_back()`** ：移除末尾元素。
* **`insert()`** ：在指定位置插入元素。
* **`erase()`** ：移除指定位置的元素或范围内的元素。
* **`clear()`** ：移除所有元素。

```cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec = {1, 2, 3};

    // 在末尾添加元素
    vec.push_back(4);  // vec: {1, 2, 3, 4}

    // 移除末尾元素
    vec.pop_back();    // vec: {1, 2, 3}

    // 在指定位置插入元素
    vec.insert(vec.begin() + 1, 10);  // vec: {1, 10, 2, 3}

    // 移除指定位置的元素
    vec.erase(vec.begin() + 2);       // vec: {1, 10, 3}

    // 清空所有元素
    vec.clear();                      // vec: {}

    return 0;
}
```

### 5. **遍历 `vector`**

可以使用迭代器或范围 `for` 循环遍历 `vector`：

```cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // 使用迭代器遍历
    for (std::vector<int>::iterator it = vec.begin(); it != vec.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;

    // 使用范围 for 循环遍历
    for (const auto& elem : vec) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

### 6. **获取大小和容量**

`std::vector` 提供了以下方法来获取其大小和容量：

* **`size()`** ：返回当前元素的数量。
* **`capacity()`** ：返回在不重新分配内存的情况下，`vector` 可以容纳的元素数量。
* **`empty()`** ：如果 `vector` 为空，返回 `true`，否则返回 `false`。

```cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec = {1, 2, 3};

    std::cout << "Size: " << vec.size() << std::endl;        // 输出: Size: 3
    std::cout << "Capacity: " << vec.capacity() << std::endl; // 输出: Capacity: 3 或更大
    std::cout << "Is empty: " << std::boolalpha << vec.empty() << std::endl; // 输出: Is empty: false

    return 0;
}
```

### 7. **预留和调整容量**

可以使用 `reserve()` 方法预留内存，以减少多次重新分配的开销：

```cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec;
    vec.reserve(100);  // 预留空间以容纳 100 个元素

    for (int i = 0; i < 100; ++i) {
        vec.push_back(i);
    }

    std::cout << "Size: " << vec.size() << std::endl;        // 输出: Size: 100
    std::cout << "Capacity: " << vec.capacity() << std::endl; // 输出: Capacity: 100 或更大

    return 0;
}
```

**注意：** `reserve()` 只增加容量，不改变实际元素的数量；而 `resize()` 可以改变 `vector` 的大小，并初始化新增的元素。

## hash

在C++中，哈希表（Hash Table）是一种通过哈希函数将关键字映射到表中位置，以实现高效数据存取的数据结构。C++标准库提供了无序关联容器（unordered associative containers），如 `std::unordered_map` 和 `std::unordered_set`，它们是基于哈希表实现的。

**使用 `std::unordered_map`：**

`std::unordered_map` 是一个关联容器，用于存储键值对（key-value pairs），其中键是唯一的。其主要特点包括：

* **无序性** ：元素在容器中的存储顺序是无序的。
* **快速查找** ：平均情况下，查找、插入和删除操作的时间复杂度为 O(1)。

**示例：**

```cpp
#include <iostream>
#include <unordered_map>
#include <string>

int main() {
    // 创建一个 unordered_map，键类型为 std::string，值类型为 int
    std::unordered_map<std::string, int> fruitMap;

    // 插入元素
    fruitMap["apple"] = 1;
    fruitMap["banana"] = 2;
    fruitMap["cherry"] = 3;

    // 查找并输出元素
    std::string key = "banana";
    auto it = fruitMap.find(key);
    if (it != fruitMap.end()) {
        std::cout << "Key: " << key << ", Value: " << it->second << std::endl;
    } else {
        std::cout << "Key not found." << std::endl;
    }

    // 遍历并输出所有元素
    for (const auto& pair : fruitMap) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    return 0;
}
```

**输出：**

```
Key: banana, Value: 2
apple: 1
banana: 2
cherry: 3
```

**注意事项：**

* **头文件** ：使用 `std::unordered_map` 需要包含头文件 `<unordered_map>`。
* **哈希函数** ：对于内置类型（如 `int`、`std::string`）的键，C++标准库提供了默认的哈希函数。如果使用自定义类型作为键，需要为该类型提供哈希函数。例如：

```cpp
struct CustomType {
    int id;
    std::string name;
};

// 自定义哈希函数
struct CustomHash {
    std::size_t operator()(const CustomType& obj) const {
        std::size_t h1 = std::hash<int>{}(obj.id);
        std::size_t h2 = std::hash<std::string>{}(obj.name);
        return h1 ^ (h2 << 1); // 合并哈希值
    }
};
```

然后，在定义 `std::unordered_map` 时，指定自定义哈希函数：

```cpp
std::unordered_map<CustomType, ValueType, CustomHash> customMap;
```

* **冲突处理** ：当不同的键通过哈希函数映射到相同的位置时，会发生哈希冲突。`std::unordered_map` 内部采用链地址法（separate chaining）来处理冲突，即在同一桶（bucket）中使用链表或其他结构存储多个元素。
* **性能考虑** ：虽然平均情况下操作时间复杂度为 O(1)，但在最坏情况下（例如大量哈希冲突），时间复杂度可能退化为 O(n)。因此，选择合适的哈希函数和合理的桶数量对于性能至关重要。

### 删除元素

```python
#include <iostream>
#include <unordered_map>

int main() {
    std::unordered_map<std::string, int> myMap;
    myMap["apple"] = 1;
    myMap["banana"] = 2;
    myMap["cherry"] = 3;

    // 删除键为 "banana" 的元素
    myMap.erase("banana");

    // 输出剩余元素
    for (const auto& pair : myMap) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    return 0;
}

```

### 查看大小

```cpp
#include <iostream>
#include <unordered_map>

int main() {
    std::unordered_map<std::string, int> myMap;
    myMap["apple"] = 1;
    myMap["banana"] = 2;
    myMap["cherry"] = 3;

    // 获取哈希表中元素的数量
    std::cout << "Size of myMap: " << myMap.size() << std::endl;

    return 0;
}
```

```
Size of myMap: 3
```

**关于“大小”的含义：**

在哈希表中，“大小”通常有两个含义：

1. **元素数量（size）：** 哈希表中当前存储的键值对（元素）数量。
2. **桶数量（bucket count）：** 哈希表内部用于存储元素的桶（bucket）数量。桶的数量影响哈希表的性能，过少的桶可能导致更多的冲突，过多的桶可能浪费空间。

您可以使用以下代码获取桶数量：

```cpp
std::cout << "Bucket count: " << myMap.bucket_count() << std::endl;
```

## queue

 `std::queue` 的基本用法示例：

```cpp
#include <iostream>
#include <queue>

int main() {
    // 创建一个整数类型的队列
    std::queue<int> q;

    // 向队列尾部添加元素
    q.push(10);
    q.push(20);
    q.push(30);

    // 输出队列中的元素数量
    std::cout << "队列中的元素数量: " << q.size() << std::endl;

    // 输出队首元素
    std::cout << "队首元素: " << q.front() << std::endl;

    // 输出队尾元素
    std::cout << "队尾元素: " << q.back() << std::endl;

    // 移除队首元素
    q.pop();
    std::cout << "移除队首元素后，队首元素: " << q.front() << std::endl;

    // 再次输出队列中的元素数量
    std::cout << "队列中的元素数量: " << q.size() << std::endl;

    return 0;
}
```

输出结果：

```
队列中的元素数量: 3
队首元素: 10
队尾元素: 30
移除队首元素后，队首元素: 20
队列中的元素数量: 2
```

**常用成员函数：**

* `push(const value_type& val)`：将元素 `val` 添加到队列尾部。
* `pop()`：移除队列头部的元素。
* `front()`：返回对队列头部元素的引用。
* `back()`：返回对队列尾部元素的引用。
* `empty()`：检查队列是否为空。
* `size()`：返回队列中元素的数量。

**注意事项：**

* `std::queue` 不提供迭代器，因此无法像其他 STL 容器那样使用范围-based for 循环或迭代器进行遍历。要遍历队列中的元素，需要在移除元素的同时访问它们，例如：

  ```cpp
  while (!q.empty()) {
      std::cout << q.front() << " ";
      q.pop();
  }
  std::cout << std::endl;
  ```

# c++好用的函数

## 字符判断函数

C++ 标准库中提供了一些非常实用的函数，用来判断字符是否是字母、数字、空格等等。这些函数都在头文件 `<cctype>`（C 风格）中。

---

### 📚 常用字符判断函数（来自 `<cctype>`）：

| 函数名          | 作用说明                                 |
| --------------- | ---------------------------------------- |
| `isalpha(c)`  | 判断是否为字母（a~z 或 A~Z）            |
| `isdigit(c)`  | 判断是否为数字（0~9）                    |
| `isalnum(c)`  | 判断是否为字母或数字（字母+数字）        |
| `islower(c)`  | 判断是否为小写字母                       |
| `isupper(c)`  | 判断是否为大写字母                       |
| `isspace(c)`  | 判断是否为空白字符（空格、换行等）       |
| `ispunct(c)`  | 判断是否为标点符号                       |
| `isxdigit(c)` | 判断是否为十六进制字符（0~9, a~f, A~F） |
| `isprint(c)`  | 判断是否为可打印字符                     |
| `iscntrl(c)`  | 判断是否为控制字符                       |

---

### ✅ 示例代码：

```cpp
#include <iostream>
#include <cctype>  // 包含字符处理函数

int main() {
    char ch = 'A';

    if (isalpha(ch)) {
        std::cout << ch << " 是字母" << std::endl;
    }

    if (isdigit(ch)) {
        std::cout << ch << " 是数字" << std::endl;
    }

    if (isalnum(ch)) {
        std::cout << ch << " 是字母或数字" << std::endl;
    }

    if (isupper(ch)) {
        std::cout << ch << " 是大写字母" << std::endl;
    }

    ch = ' ';
    if (isspace(ch)) {
        std::cout << "这是一个空格" << std::endl;
    }

    return 0;
}
```

## ## 字符串转数字

在 C++ 中，可以使用多种方法将字符串转换为数字，主要包括 `std::stoi`、`std::atof`、`std::atoi` 等函数。以下是这些函数的详细介绍和使用示例：

### 1. 使用 `std::stoi` 函数

`std::stoi`（string to integer）是 C++11 引入的标准库函数，用于将 `std::string` 转换为整数。其函数签名为：

```cpp
int stoi(const std::string& str, std::size_t* pos = nullptr, int base = 10);
```

* `str`：要转换的字符串。
* `pos`：指向 `size_t` 的指针，用于存储转换结束的位置索引，可选参数，默认为 `nullptr`。
* `base`：转换所使用的进制，默认为 10。

**示例：**

```cpp
#include <iostream>
#include <string>

int main() {
    std::string str = "12345";
    try {
        int num = std::stoi(str);
        std::cout << "转换后的数字为：" << num << std::endl;
    } catch (const std::invalid_argument& e) {
        std::cerr << "无效的输入：" << e.what() << std::endl;
    } catch (const std::out_of_range& e) {
        std::cerr << "输入超出范围：" << e.what() << std::endl;
    }
    return 0;
}
```

**注意：**

* 如果输入字符串不是有效的数字表示，`std::stoi` 会抛出 `std::invalid_argument` 异常。
* 如果转换结果超出了 `int` 类型的表示范围，会抛出 `std::out_of_range` 异常。 citeturn0search6

### 2. 使用 `std::atoi` 函数

`std::atoi`（ASCII to integer）是 C 标准库函数，可在 C++ 中使用，用于将 C 风格的字符串（即以空字符 `'\0'` 结尾的字符数组）转换为整数。其函数签名为：

```cpp
int atoi(const char* str);
```

**示例：**

```cpp
#include <iostream>
#include <cstdlib>

int main() {
    const char* str = "6789";
    int num = std::atoi(str);
    std::cout << "转换后的数字为：" << num << std::endl;
    return 0;
}
```

**注意：**

* `std::atoi` 不会进行错误检查，如果输入字符串不是有效的数字，返回值未定义。
* 不建议在现代 C++ 中使用 `std::atoi`，因为它缺乏错误处理机制，建议使用 `std::stoi` 替代。 citeturn0search4

### 3. 使用 `std::atof` 函数

`std::atof`（ASCII to float）用于将 C 风格的字符串转换为浮点数。其函数签名为：

```cpp
double atof(const char* str);
```

**示例：**

```cpp
#include <iostream>
#include <cstdlib>

int main() {
    const char* str = "3.14159";
    double num = std::atof(str);
    std::cout << "转换后的数字为：" << num << std::endl;
    return 0;
}
```

**注意：**

* 与 `std::atoi` 类似，`std::atof` 也缺乏错误处理机制，建议在现代 C++ 中使用 `std::stod`（string to double）替代。 citeturn0search9

### 4. 使用 `std::stringstream` 类

`std::stringstream` 是 C++ 标准库中的类，可用于将字符串转换为各种数值类型。

**示例：**

```cpp
#include <iostream>
#include <sstream>
#include <string>

int main() {
    std::string str = "42";
    int num;
    std::stringstream ss(str);
    ss >> num;
    if (ss.fail()) {
        std::cerr << "转换失败" << std::endl;
    } else {
        std::cout << "转换后的数字为：" << num << std::endl;
    }
    return 0;
}
```

**注意：**

* 使用 `std::stringstream` 进行转换时，需要检查流的状态以确保转换成功。

### 总结

在 C++ 中，推荐使用 `std::stoi`、`std::stod` 等现代函数进行字符串到数字的转换，因为它们提供了异常处理机制，能够更安全地处理错误情况。而 `std::atoi`、`std::atof` 等 C 风格的函数由于缺乏错误处理机制，不建议在现代 C++ 中使用。

# python迭代器用法

## set

在 Python 中，`set` 是一个非常常用的数据类型，它表示一个无序的集合，且集合中的元素是 **唯一** 的，不能重复。`set` 是 Python 中的一种内建数据结构，它与数学中的集合类似，可以进行集合的基本操作，如交集、并集、差集等。

### 基本用法

#### 1. **创建集合**

你可以使用 `{}` 或 `set()` 来创建一个集合。

```python
# 使用花括号创建集合
my_set = {1, 2, 3, 4, 5}
print(my_set)  # 输出: {1, 2, 3, 4, 5}

# 使用 set() 函数创建集合
my_set2 = set([1, 2, 2, 3, 4])  # 重复的元素会被去除
print(my_set2)  # 输出: {1, 2, 3, 4}
```

#### 2. **添加元素**

使用 `add()` 方法可以向集合中添加单个元素。如果该元素已经存在，集合不会发生变化。

```python
my_set.add(6)
print(my_set)  # 输出: {1, 2, 3, 4, 5, 6}
```

#### 3. **删除元素**

使用 `remove()` 或 `discard()` 方法删除元素。`remove()` 在删除元素时，如果该元素不存在，会抛出 `KeyError` 异常；`discard()` 如果元素不存在不会报错。

```python
my_set.remove(3)  # 删除元素 3
print(my_set)  # 输出: {1, 2, 4, 5, 6}

my_set.discard(7)  # 该元素不存在，不会报错
print(my_set)  # 输出: {1, 2, 4, 5, 6}
```

#### 4. **集合的基本操作**

* **交集** (`&` 或 `intersection()`)
* **并集** (`|` 或 `union()`)
* **差集** (`-` 或 `difference()`)
* **对称差集** (`^` 或 `symmetric_difference()`)

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 交集
intersection = set1 & set2
print("Intersection:", intersection)  # 输出: {3, 4}

# 并集
union = set1 | set2
print("Union:", union)  # 输出: {1, 2, 3, 4, 5, 6}

# 差集
difference = set1 - set2
print("Difference (set1 - set2):", difference)  # 输出: {1, 2}

# 对称差集
symmetric_difference = set1 ^ set2
print("Symmetric Difference:", symmetric_difference)  # 输出: {1, 2, 5, 6}
```

#### 5. **检查元素是否在集合中**

你可以使用 `in` 关键字来检查元素是否在集合中。

```python
print(3 in my_set)  # 输出: True
print(7 in my_set)  # 输出: False
```

#### 6. **集合的其他常用方法**

* **`len()`** : 获取集合的大小。
* **`clear()`** : 清空集合。
* **`copy()`** : 复制集合。

```python
# 获取集合的大小
print(len(my_set))  # 输出: 5

# 清空集合
my_set.clear()
print(my_set)  # 输出: set()

# 复制集合
set_copy = my_set2.copy()
print(set_copy)  # 输出: {1, 2, 3, 4}
```

### 示例：集合的常见操作

```python
# 创建集合
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 交集
print("Intersection:", set1 & set2)  # {4, 5}

# 并集
print("Union:", set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8}

# 差集
print("Difference:", set1 - set2)  # {1, 2, 3}

# 对称差集
print("Symmetric Difference:", set1 ^ set2)  # {1, 2, 3, 6, 7, 8}
```

### 注意：

* 集合中的元素是  **无序的** ，意味着你不能通过索引访问集合中的元素。
* 集合中的元素是  **唯一的** ，重复元素会被自动去除。
* 集合支持快速的 **查找、插入、删除** 操作，通常复杂度为 `O(1)`。

### 总结：

Python 中的 `set` 提供了高效的集合操作，可以处理交集、并集、差集等集合运算，非常适合用于处理去重、查找和集合运算等任务。
