package kr.co.aiai.dao;
import java.sql.*;


public class Myupdate {

	public static void main(String[] args) throws Exception {

		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python", "root", "python");
		Statement stmt = conn.createStatement();
		String sql = "UPDATE emp SET e_name=1, sex=1, addr=1 WHERE e_id = 2";
				
		
	
		stmt = conn.prepareStatement(sql);
		int result = stmt.executeUpdate(sql);
		// 3. 결과 확인
		System.out.println("결과 : " + result);

 
		
		stmt.close();
		conn.close();
	}
}



