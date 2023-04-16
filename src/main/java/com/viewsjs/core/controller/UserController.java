package com.viewsjs.core.controller;

import com.viewsjs.core.repository.UserRepository;
import com.viewsjs.core.model.User;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import java.util.List;

@Controller
public class UserController {

    UserRepository userRepository;

    public UserController(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @QueryMapping
    public List<User> users() {
        return (List<User>) userRepository.findAll();
    }
}
