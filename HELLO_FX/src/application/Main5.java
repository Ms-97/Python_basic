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


public class Main5 extends Application {
	
	TextField tfm;
	TextField tfc;
	TextField tfr;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("main5.fxml"));

			Scene scene = new Scene(root,400,400);
			
			tfm = (TextField) scene.lookup("#tf_mine");
			tfc = (TextField) scene.lookup("#tf_com");
			tfr = (TextField) scene.lookup("#tf_result");
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
		
		String user = tfm.getText();
		Random random = new Random();
		int rnd = random.nextInt(2);
		
		String com = "";
		if(rnd == 0) {
			com = "홀";
		}else {
			com = "짝";
		}
		
		tfc.setText(com);
		
		if(com.equals(user)) {
			tfr.setText("유저승리");
		}else {
			tfr.setText("com승리");
		}
		
	}
	
	public void myclicksem() {
		String com = "";
		String mine = "";
		String result ="";
		
		mine = tfm.getText();
		
		double rnd = Math.random();
		
		if(rnd >0.5) {
			com = "홀";
		} else {
			com = "짝";
		}
		
		if(com.equals(mine)) {
			result = "이김";
		} else {
			result = "짐";
		}
		tfc.setText(com);
		tfr.setText(result);
		
	}
	
	
	public static void main(String[] args) {
		launch(args);
	}
}
