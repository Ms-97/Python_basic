package kr.co.aiai.dao;
import java.sql.*;


public class MyInsert {

	public static void main(String[] args) throws Exception {

		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python", "root", "python");
		Statement stmt = conn.createStatement();
		String sql = "insert into emp (e_id,e_name,sex,addr) values (3,3,3,3)";
		
	
		PreparedStatement pstmt = conn.prepareStatement(sql);
		int result = pstmt.executeUpdate();
		// 3. 결과 확인
		System.out.println("결과 : " + result);


		
		pstmt.close();
		conn.close();
	}
}



