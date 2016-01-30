template<typename T>
class array{
 public:
  int size;
  T* container;

  array ( int s){
    container = new T[s];
    size = s;
    //copy to container
  }
  
  T & operator[](int i){
    return container[i];
  }

  ~array (){
    delete[] container;
  }
};
