//
//  ContentView.swift
//  ToDoList-FastAPI
//
//  Created by Mamdouh Aldhafeeri on 17/09/2023.
//
   
import SwiftUI

struct MainView: View {
    var body: some View {
        NavigationView {
            LoginView()
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        MainView()
    }
}
