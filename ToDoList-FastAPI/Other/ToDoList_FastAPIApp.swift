//
//  ToDoList_FastAPIApp.swift
//  ToDoList-FastAPI
//
//  Created by Mamdouh Aldhafeeri on 17/09/2023.
//

import FirebaseCore
import SwiftUI

@main
struct ToDoList_FastAPIApp: App {
    init(){
        FirebaseApp.configure()
    }
    
    var body: some Scene {
        WindowGroup {
            MainView()
        }
    }
}
