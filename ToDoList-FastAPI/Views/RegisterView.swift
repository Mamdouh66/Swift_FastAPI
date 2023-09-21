//
//  RegisterView.swift
//  ToDoList-FastAPI
//
//  Created by Mamdouh Aldhafeeri on 17/09/2023.
//

import SwiftUI

struct RegisterView: View {
    var body: some View {
        VStack {
            // Header
            HeaderView(title: "Register", subtitle: "Make an account with us", angle: -15, backgroundColor: .orange)
        }
    }
}

struct RegisterView_Previews: PreviewProvider {
    static var previews: some View {
        RegisterView()
    }
}
