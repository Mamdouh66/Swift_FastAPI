//
//  HeaderView.swift
//  ToDoList-FastAPI
//
//  Created by Mamdouh Aldhafeeri on 17/09/2023.
//

import SwiftUI

struct HeaderView: View {
    let title : String
    let subtitle : String
    let angle : Double
    let backgroundColor : Color
    
    var body: some View {
        ZStack {
            RoundedRectangle(cornerRadius: 0)
                .foregroundColor(backgroundColor)
                .rotationEffect(Angle(degrees : angle))
            
            VStack {
                Text(title)
                    .foregroundColor(Color.white)
                    .bold()
                    .font(.system(size: 50))
                
                Text(subtitle)
                    .font(.system(size: 30))
                    .foregroundColor(Color.white)
            }
            .padding(.top, 30)
        }
        .frame(width: UIScreen.main.bounds.width * 3,
               height: 300)
        .offset(y: -100)

    }
}

struct HeaderView_Previews: PreviewProvider {
    static var previews: some View {
        HeaderView(title: "Title",
                   subtitle: "Subtitle",
                   angle: 15,
                   backgroundColor: .blue)
    }
}
