package day23;

public class MyRef {
	
	public static void changeInt(int a) {
		a = 3;
	}
	public static void changeArr(int[] a) {
		a[0] = 3;
	}
	
	public static void main(String[] args) {
		int b = 1;
		int[] bb = {1};
		
		System.out.println(b);
		System.out.println(bb[0]);
		
		changeInt(b);
		changeArr(bb);
		
		System.out.println(b);
		System.out.println(bb[0]);
	}
}
