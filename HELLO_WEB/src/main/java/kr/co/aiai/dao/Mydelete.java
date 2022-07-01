package kr.co.aiai.dao;
import java.sql.*;


public class Mydelete {

	public static void main(String[] args) throws Exception {

		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python", "root", "python");
		Statement stmt = conn.createStatement();
		String sql = "DELETE from emp where e_id = 3";
		
	
		PreparedStatement pstmt = conn.prepareStatement(sql);
		int result = pstmt.executeUpdate();
		// 3. 결과 확인
		System.out.println("결과 : " + result);


		
		pstmt.close();
		conn.close();
	}
}



