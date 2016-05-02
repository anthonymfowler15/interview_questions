import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BeerProfit {
  static final int DAYS = 7;

  // orders=[
  //   {"brewery": "la_brew", "kegs": 5, "type": "pilsner"},
  //   {"brewery": "sf_brewery_united", "kegs": 2, "type": "ipa"},
  //   {"brewery": "sunnyvale_hipster_bar", "kegs": 10, "type": "lambic"}
  // ]
  private static List getOrders() {
    List< Order > orders= new ArrayList < Order >();
    Order order1 = new Order("la_brew", 5, "pilsner");
    Order order2 = new Order("sf_brewery_united", 2, "ipa");
    Order order3 = new Order("sunnyvale_hipster_bar", 10, "lambic");

    orders.add(order1);
    orders.add(order2);
    orders.add(order3);
    return orders;
  }

  // time_table = {'pilsner': 1, 'ipa': 2, 'lambic': 5}
  private static Map getTimeTable() {
    Map<String, Integer> time_table = new HashMap<String, Integer>();
    time_table.put("pilsner", 1);
    time_table.put("ipa", 2);
    time_table.put("lambic", 5);
    return time_table;
  }

  // profit_table = {'pilsner': 5, 'ipa': 15, 'lambic': 10}
  private static Map getProfitTable() {
    Map<String, Integer> profit_table = new HashMap<String, Integer>();
    profit_table.put("pilsner", 5);
    profit_table.put("ipa", 15);
    profit_table.put("lambic", 10);
    return profit_table;
  }

  public static void main(String[] args) {
    List< Order > orders = getOrders();
    Map <String, Integer> time_table = getTimeTable();
    Map <String, Integer> profit_table = getProfitTable();

    // how do you maximize profit? What is the maximum profit that we can get from this list of orders?
    // Assume you can make any number of kegs in an order
    // Assume each beer type is only requested once
    // Solution
    Result result = findProfit(0, orders, new ArrayList<Order>(), DAYS, time_table, profit_table);
    System.out.println(result.profit);
    System.out.println(result.orders_taken);
  }

  public static Result findProfit(int profit, List <Order> order_list, List <Order> orders_taken, int days_left, Map<String, Integer> time_table, Map<String, Integer> profit_table) {
    if (order_list.size() <= 0) {
      return new Result(profit, orders_taken);
    }

    if (days_left < time_table.get(order_list.get(0).type) ) {
      return findProfit(profit, order_list.subList(1, order_list.size()), orders_taken, days_left, time_table, profit_table);
    }

    Order current_order = order_list.get(0);
    int profit_from_current_order = profit_table.get(current_order.type) * current_order.kegs;
    int days_left_if_take_order = days_left - time_table.get(current_order.type);
    List<Order> orders_taken_if_take_order = new ArrayList<Order>(orders_taken);
    orders_taken_if_take_order.add(current_order);

    Result result_if_skipped = findProfit(profit, order_list.subList(1, order_list.size()), orders_taken, days_left, time_table, profit_table);

    Result result_if_taken = findProfit(profit + profit_from_current_order, order_list.subList(1, order_list.size()), orders_taken_if_take_order, days_left_if_take_order, time_table, profit_table);

    if (result_if_skipped.profit > result_if_taken.profit) {
      return result_if_skipped;
    } else {
      return result_if_taken;
    }
  }
}


