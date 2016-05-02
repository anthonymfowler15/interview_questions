import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Result {
  int profit;
  List< Order> orders_taken;

  public Result(int profit, List orders_taken){
    this.profit = profit;
    this.orders_taken = orders_taken;
  }
}