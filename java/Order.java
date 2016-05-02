import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class Order {
  String brewery;
  int kegs;
  String type;

  public Order(String brewery, int kegs, String type){
    this.brewery = brewery;
    this.kegs = kegs;
    this.type = type;
  }
}