console.log('hello')

const likeBtn = document.querySelectorAll('.btn-like')

if (likeBtn) {
    likeBtn.forEach((btn) => {
        btn.addEventListener('click', () => {
            const postId = +btn.getAttribute('id')
            fetch('/posts/like/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').content
                },
                body: JSON.stringify({
                    'post_id': postId
                })
            })
                .then(res => res.json())
                .then(data => {
                    if (data.message === 'Like added') {
                        window.location.reload()
                    }
                })
        })
    })
}


