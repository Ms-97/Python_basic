package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;


public class Main4 extends Application {
	
	TextField tf;
	TextArea ta;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("main4.fxml"));

			Scene scene = new Scene(root,400,400);
			
			tf = (TextField) scene.lookup("#tf");
			ta = (TextArea) scene.lookup("#ta");
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
		String tnum = tf.getText();
		int dan = Integer.parseInt(tnum);
		String result = "";
		
		
			result = (dan + "*" + 1 + "=" + dan*1 +"\n");
	    	result += (dan + "*" + 2 + "=" + dan*2 +"\n");
			result += (dan + "*" + 3 + "=" + dan*3 +"\n");
			result += (dan + "*" + 4 + "=" + dan*4 +"\n");
			result += (dan + "*" + 5 + "=" + dan*5 +"\n");
			result += (dan + "*" + 6 + "=" + dan*6 +"\n");
			result += (dan + "*" + 7 + "=" + dan*7 +"\n");
			result += (dan + "*" + 8 + "=" + dan*8 +"\n");
			result += (dan + "*" + 9 + "=" + dan*9);
			
			ta.setText(result);
		}
	
		
	
	
	
	public static void main(String[] args) {
		launch(args);
	}
}
