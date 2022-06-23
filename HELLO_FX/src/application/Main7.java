package application;
	
import java.util.Random;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;


public class Main7 extends Application {
	
	TextField tfm;
	TextField tfc;
	TextField tfr;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("main7.fxml"));

			Scene scene = new Scene(root,400,400);
			
			tfm = (TextField) scene.lookup("#tfMine");
			tfc = (TextField) scene.lookup("#tfCom");
			tfr = (TextField) scene.lookup("#tfResult");
			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myclick();
				}	
			});
			
			
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void myclick() {
		Random random = new Random();
		int rnd = random.nextInt(3);
		
		String user = tfm.getText();
		String com = "";
		String winner = "";
		
		if(rnd == 0) {
			com = "가위";
		}else if(rnd == 1) {
			com = "바위";
		}else {
			com = "보";
		}
		
		
		if(user.equals(com)) {
			   winner = "무승부";
		}
		else if(com.equals("가위") && user.equals("보") 
		   || com.equals("바위") && user.equals("가위")
		   || com.equals("보") && user.equals("바위")) {
			
			winner = "com 승리";
		}
		else {
			winner = "유저 승리";
		}
		
		tfc.setText(com);
		tfr.setText(winner);
	}
	
	public void myclicksem() {
		String com = "";
		String mine = "";
		String result ="";
		
		mine = tfm.getText();
		
		double rnd = Math.random();
		
		if(rnd >0.66) {
			com = "가위";
		} else if(rnd >0.33) {
			com = "바위";
		} else {
			com = "보";
		}
		
		if(com.equals("가위")&&mine.equals("가위"))	result="비김";
		if(com.equals("가위")&&mine.equals("바위"))	result="이김";
		if(com.equals("가위")&&mine.equals("보"))		result="짐";
		
		if(com.equals("바위")&&mine.equals("가위"))	result="짐";
		if(com.equals("바위")&&mine.equals("바위"))	result="비김";
		if(com.equals("바위")&&mine.equals("보"))		result="이김";
		
		if(com.equals("보")&&mine.equals("가위"))	result="이김";
		if(com.equals("보")&&mine.equals("바위"))	result="짐";
		if(com.equals("보")&&mine.equals("보"))	result="비김";

		tfc.setText(com);
		tfr.setText(result);
		
	}
	
	
	public static void main(String[] args) {
		launch(args);
	}
}
